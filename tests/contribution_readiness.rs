//! Complete contribution-readiness acceptance. All child work is
//! phase-boundary BDD.
use std::{
    path::PathBuf,
    process::{Command, Output},
    sync::atomic::{AtomicUsize, Ordering},
};

use cucumber::{World as _, WriterExt as _, given, then, when};
static PASSED: AtomicUsize = AtomicUsize::new(0);
#[derive(Debug, Default, cucumber::World)]
struct Readiness {
    case: String,
    output: Option<Output>,
}
#[given(expr = "the adopted contribution readiness case {string}")]
fn case(world: &mut Readiness, case: String) {
    world.case = case;
}
fn exercise(world: &mut Readiness, control: bool) {
    let root = PathBuf::from(env!("CARGO_MANIFEST_DIR"));
    let path = root.join("tests/readiness/runtime.json");
    let runtime: serde_json::Value = serde_json::from_slice(
        &std::fs::read(&path).expect("whole-boundary preparation required"),
    )
    .unwrap();
    world.output = Some(
        Command::new(runtime["pythonExecutable"].as_str().unwrap())
            .arg(root.join("tests/readiness/cases.py"))
            .arg(&path)
            .arg(&world.case)
            .arg(if control { "control" } else { "positive" })
            .output()
            .expect("actual downstream consumers"),
    );
}
#[when("the real downstream application exercises the contribution")]
fn positive(world: &mut Readiness) {
    exercise(world, false);
}
#[when("the declared misleading result is exercised")]
fn control(world: &mut Readiness) {
    exercise(world, true);
}
fn assert_receipt(world: &Readiness) {
    let output = world.output.as_ref().unwrap();
    assert!(
        output.status.success(),
        "{}: stdout={} stderr={}",
        world.case,
        String::from_utf8_lossy(&output.stdout),
        String::from_utf8_lossy(&output.stderr)
    );
    let receipt: serde_json::Value =
        serde_json::from_slice(&output.stdout).unwrap();
    assert_eq!(receipt["case"], world.case);
    assert_eq!(receipt["status"], "PASS");
    assert!(
        receipt["observations"]
            .as_array()
            .is_some_and(|values| !values.is_empty())
    );
    PASSED.fetch_add(1, Ordering::SeqCst);
}
#[then("its independent compatibility obligation is satisfied")]
fn accepted(world: &mut Readiness) {
    assert_receipt(world);
}
#[then("rejection is proved without altering original sources or evidence")]
fn rejected(world: &mut Readiness) {
    assert_receipt(world);
}
fn main() {
    let root = PathBuf::from(env!("CARGO_MANIFEST_DIR"));
    let runtime_path = root.join("tests/readiness/runtime.json");
    let runtime: serde_json::Value =
        serde_json::from_slice(&std::fs::read(&runtime_path).unwrap()).unwrap();
    let repair_ids =
        ["CR47-004", "CR47-006", "CR47-007", "CR47-009", "CR47-010"];
    let repair = !runtime["repair"].is_null();
    if repair {
        assert_eq!(
            runtime["repair"]["affectedIds"],
            serde_json::json!(repair_ids),
            "only the authorized repair subset is supported"
        );
    }
    let expected_count = if repair { repair_ids.len() } else { 10 };
    let args: Vec<_> = std::env::args().collect();
    let positive = args.iter().any(|arg| arg == "@readiness47");
    let control = args.iter().any(|arg| arg == "@readiness47_negative");
    assert!(positive != control, "select exactly one adopted readiness packet");
    let path = PathBuf::from(runtime["evidence"].as_str().unwrap()).join(
        if positive {
            "functional-messages.ndjson"
        } else {
            "controls-messages.ndjson"
        },
    );
    let output = std::fs::OpenOptions::new()
        .write(true)
        .create_new(true)
        .open(path)
        .expect("exclusive evidence path");
    let sources = cucumber::parser::SourceStore::new();
    let writer =
        cucumber::writer::Basic::stdout::<Readiness>().summarized().tee(
            cucumber::writer::Messages::with_source_store::<Readiness>(
                output,
                sources.clone(),
            )
            .discard_stats_writes(),
        );
    futures::executor::block_on(
        Readiness::cucumber()
            .with_filter_options(cucumber::FilterOptions::new())
            .max_concurrent_scenarios(1)
            .with_source_store(sources)
            .with_writer(writer)
            .fail_on_skipped()
            .filter_run_and_exit(
                root.join("tests/features/contribution_readiness"),
                move |_, _, scenario| {
                    !repair
                        || scenario.tags.iter().any(|tag| {
                            repair_ids.contains(&tag.trim_start_matches('@'))
                        })
                },
            ),
    );
    assert_eq!(
        PASSED.load(Ordering::SeqCst),
        expected_count,
        "zero/partial/unfiltered readiness scope is not accepted"
    );
    if control {
        let result =
            Command::new(runtime["pythonExecutable"].as_str().unwrap())
                .arg(root.join("tests/readiness/finalize.py"))
                .arg(&runtime_path)
                .output()
                .unwrap();
        println!("{}", String::from_utf8_lossy(&result.stdout));
        eprintln!("{}", String::from_utf8_lossy(&result.stderr));
        assert!(result.status.success(), "complete-packet finalization failed");
    }
}
