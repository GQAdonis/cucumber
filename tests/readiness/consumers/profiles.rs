//! An external application, compiled separately for each adopted feature
//! profile.
use std::sync::{
    Arc, Mutex,
    atomic::{AtomicUsize, Ordering},
};

#[cfg(feature = "macros")]
use cucumber::World as _;
use cucumber::{StatsWriter as _, WriterExt as _, writer};
use serde_json::{Value, json};

static EFFECTS: AtomicUsize = AtomicUsize::new(0);
#[derive(Debug, Default)]
#[cfg_attr(feature = "macros", derive(cucumber::World))]
struct Application;
#[cfg(not(feature = "macros"))]
impl cucumber::World for Application {
    type Error = std::convert::Infallible;
    async fn new() -> Result<Self, Self::Error> {
        Ok(Self)
    }
}
fn effect() {
    EFFECTS.fetch_add(1, Ordering::SeqCst);
    #[cfg(feature = "tracing")]
    tracing::info!("profile handler evidence");
}
#[cfg(feature = "macros")]
#[cucumber::given("a registered application action")]
fn registered(_: &mut Application) {
    effect();
}
#[cfg(not(feature = "macros"))]
fn registered(
    _: &mut Application,
    _: cucumber::step::Context,
) -> futures::future::LocalBoxFuture<'_, ()> {
    Box::pin(async {
        effect();
    })
}
#[derive(Clone)]
struct Events(Arc<Mutex<Vec<Value>>>);
impl cucumber::Writer<Application> for Events {
    type Cli = cucumber::cli::Empty;
    async fn handle_event(
        &mut self,
        event: cucumber::parser::Result<
            cucumber::Event<cucumber::event::Cucumber<Application>>,
        >,
        _: &Self::Cli,
    ) {
        match event {
            Ok(event) => {
                let mut observation =
                    json!({"event": format!("{:?}", event.value)});
                #[cfg(any(
                    feature = "timestamps",
                    feature = "output-json",
                    feature = "output-junit",
                    feature = "libtest",
                    feature = "output-messages"
                ))]
                {
                    observation["timestampNanos"] = json!(
                        event
                            .at
                            .duration_since(std::time::UNIX_EPOCH)
                            .unwrap()
                            .as_nanos()
                            .to_string()
                    );
                }
                // Keep the declaration warning-free in the profiles without
                // timestamps.
                observation["observed"] = json!(true);
                self.0.lock().unwrap().push(observation);
            }
            Err(error) => self
                .0
                .lock()
                .unwrap()
                .push(json!({"parseError":error.to_string()})),
        }
    }
}
async fn run(path: &str) -> Value {
    #[cfg(feature = "macros")]
    let steps = Application::collection();
    #[cfg(not(feature = "macros"))]
    let steps = cucumber::step::Collection::new().given(
        None,
        regex::Regex::new("^a registered application action$").unwrap(),
        registered,
    );
    let events = Arc::new(Mutex::new(Vec::new()));
    let mut basic_output = Vec::new();
    let writer =
        writer::Basic::raw(&mut basic_output, writer::Coloring::Never, 0)
            .tee::<Application, _>(
                Events(Arc::clone(&events))
                    .discard_stats_writes()
                    .discard_arbitrary_writes(),
            )
            .normalized()
            .summarized();
    #[cfg(any(
        feature = "output-json",
        feature = "output-junit",
        feature = "libtest",
        feature = "output-messages"
    ))]
    let mut special_output = Vec::new();
    #[cfg(feature = "output-json")]
    let writer = writer.tee(
        writer::Json::new::<Application>(&mut special_output)
            .discard_stats_writes(),
    );
    #[cfg(feature = "output-junit")]
    let writer = writer.tee(
        writer::JUnit::<Application, _>::new(&mut special_output, 0)
            .discard_stats_writes(),
    );
    #[cfg(feature = "libtest")]
    let writer = writer.tee(
        writer::Libtest::<Application, _>::new(&mut special_output)
            .discard_stats_writes(),
    );
    #[cfg(feature = "output-messages")]
    let sources = cucumber::parser::SourceStore::new();
    #[cfg(feature = "output-messages")]
    let writer = writer.tee(
        writer::Messages::with_source_store::<Application>(
            &mut special_output,
            sources.clone(),
        )
        .discard_stats_writes(),
    );
    let application = cucumber::Cucumber::new()
        .steps(steps)
        .with_writer(writer)
        .max_concurrent_scenarios(1)
        .fail_on_skipped();
    #[cfg(feature = "output-messages")]
    let application = application.with_source_store(sources);
    #[cfg(feature = "tracing")]
    let application = application.init_tracing();
    let report = application.with_default_cli().run(path).await;
    let statistics = json!({
    "passed":report.passed_steps(),
    "failed":report.failed_steps(),

    "skipped":report.skipped_steps(),
        "parsingErrors":report.parsing_errors(),

    "hookErrors":report.hook_errors(),
        "executionFailed":report.execution_has_failed()}
        );
    drop(report);
    #[cfg(any(
        feature = "output-json",
        feature = "output-junit",
        feature = "libtest",
        feature = "output-messages"
    ))]
    let special = String::from_utf8(special_output).unwrap();
    #[cfg(not(any(
        feature = "output-json",
        feature = "output-junit",
        feature = "libtest",
        feature = "output-messages"
    )))]
    let special = String::new();
    let mut result = statistics;
    result["sideEffects"] = json!(EFFECTS.load(Ordering::SeqCst));
    result["basic"] = json!(String::from_utf8(basic_output).unwrap());
    result["special"] = json!(special);
    result["events"] = json!(*events.lock().unwrap());
    result
}
fn main() {
    let path = std::env::args().nth(1).expect("application feature path");
    println!("{}", futures::executor::block_on(run(&path)));
}
