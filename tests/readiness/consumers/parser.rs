//! External parser API consumer, built separately against
//! immutable/fork/vendor sources.
use std::{io::Read as _, path::Path};

use gherkin::{Feature, GherkinEnv, ParseFileError};
use serde_json::{Value, json};

fn project(feature: &Feature) -> Value {
    json!({
        "name":feature.name,
        "scenarios":feature.scenarios.iter().map(|scenario|json!({
        
        "name":scenario.name,
            "steps":scenario.steps.iter().map(|step|json!({
            "text":step.value,
            
        "table":step.table.as_ref().map(|table|&table.rows),
            "docstring":step.docstring}
            )).collect::<Vec<_>>(),
            
        "examples":scenario.examples.iter().map(|examples|examples.table.as_ref().map(|table|&table.rows)).collect::<Vec<_>>()
    })).collect::<Vec<_>>()})
}
fn env(policy: &str) -> GherkinEnv {
    match policy {
        "default" => GherkinEnv::default(),
        "new" => GherkinEnv::new("en").unwrap(),
        #[cfg(feature = "modern")]
        "latest" => GherkinEnv::new_latest("en").unwrap(),
        #[cfg(feature = "modern")]
        "explicit43" => GherkinEnv::new_latest("en")
            .unwrap()
            .with_table_semantics(gherkin::TableSemantics::Gherkin43),
        _ => panic!("unsupported policy"),
    }
}
fn file_error(error: ParseFileError) -> Value {
    let display = error.to_string();
    match error {
        ParseFileError::Reading { path, source } => {
            json!({
            "ok":false,
            "variant":"Reading",
            "path":path,
            "display":display,
            "ioKind":format!("{:?}",
            source.kind())}
            )
        }
        ParseFileError::Parsing { path, error, source } => {
            let detail = source.to_string();
            #[cfg(feature = "modern")]
            let position = json!({
            "line":source.position().line,
            "column":source.position().col}
            );
            #[cfg(not(feature = "modern"))]
            let position = {
                let coordinate = detail
                    .strip_prefix("Error at ")
                    .unwrap()
                    .split(": ")
                    .next()
                    .unwrap();
                let (line, column) = coordinate.split_once(':').unwrap();
                json!({
                "line":line.parse::<usize>().unwrap(),
                "column":column.parse::<usize>().unwrap()}
                )
            };
            json!({
                "ok":false,
                "variant":"Parsing",
                "path":path,
                "display":display,
                "diagnostic":detail,
                "position":position,
                
                "environment":error.map(|error|error.to_string())})
        }
    }
}
fn dispatch(request: &Value) -> Value {
    let policy = request["policy"].as_str().unwrap_or("default");
    match request["operation"].as_str().unwrap() {
        "parse" => match Feature::parse(
            request["source"].as_str().unwrap(),
            env(policy),
        ) {
            Ok(feature) => json!({"ok":true,"feature":project(&feature)}),
            Err(error) => json!({"ok":false,"diagnostic":error.to_string()}),
        },
        "file" => match Feature::parse_path(
            Path::new(request["path"].as_str().unwrap()),
            env(policy),
        ) {
            Ok(feature) => {
                json!({
                "ok":true,
                "feature":project(&feature),
                "path":feature.path}
                )
            }
            Err(error) => file_error(error),
        },
        #[cfg(feature = "modern")]
        "document" => match gherkin::Document::parse(
            request["source"].as_str().unwrap(),
            env(policy),
        ) {
            Ok(document) => {
                json!({
                "ok":true,
                "feature":document.feature.as_ref().map(project)}
                )
            }
            Err(error) => json!({"ok":false,"diagnostic":error.to_string()}),
        },
        #[cfg(feature = "modern")]
        "markdown" => match gherkin::markdown::MarkdownDocument::parse(
            request["source"].as_str().unwrap(),
            "en",
        ) {
            Ok(document) => {
                json!({
                "ok":true,
                "feature":document.to_feature().as_ref().map(project)}
                )
            }
            Err(error) => {
                json!({
                "ok":false,
                "diagnostic":error.to_string(),
                "position":{
                "line":error.position.line,
                "column":error.position.col}
                }
                )
            }
        },
        _ => panic!("unsupported request"),
    }
}
fn main() {
    let mut text = String::new();
    std::io::stdin().read_to_string(&mut text).unwrap();
    let requests: Vec<Value> = serde_json::from_str(&text).unwrap();
    println!(
        "{}",
        json!({
        "responses":requests.iter().map(dispatch).collect::<Vec<_>>(),
        "manifestDir":env!("CARGO_MANIFEST_DIR")}
        )
    );
}
