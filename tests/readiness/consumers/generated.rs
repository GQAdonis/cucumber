//! Real derived/default-generic and custom-initialized consumer Worlds.
use std::{
    fmt::Debug,
    path::Path,
    sync::{Arc, LazyLock, Mutex},
    time::Duration,
};

use cucumber::{
    World as _, WriterExt as _,
    attachment::{
        Attachment, AttachmentContext, AttachmentHandle, AttachmentStore,
    },
    execution::{
        Completion, ExecutionControl, ExecutionHandle, OutcomePolicy,
        WorldContext,
    },
    runner::{TimeoutClock, TimeoutPolicy, Timeouts},
    step::{Collection, Context, DefinitionOptions},
};
use futures::future::{BoxFuture, LocalBoxFuture};
use regex::Regex;
use serde_json::{Value, json};

static TRACE: LazyLock<Mutex<Vec<String>>> = LazyLock::new(Default::default);
static TIMERS: Mutex<Vec<u128>> = Mutex::new(Vec::new());
static OLD_ATTACHMENT: Mutex<Option<AttachmentHandle>> = Mutex::new(None);
static OLD_COMPLETION: Mutex<Option<ExecutionHandle>> = Mutex::new(None);
fn trace(value: impl Into<String>) {
    TRACE.lock().unwrap().push(value.into());
}
fn take_trace() -> Vec<String> {
    std::mem::take(&mut *TRACE.lock().unwrap())
}
fn messages(bytes: Vec<u8>) -> Vec<Value> {
    String::from_utf8(bytes)
        .unwrap()
        .lines()
        .map(|line| serde_json::from_str(line).unwrap())
        .collect()
}
#[derive(Debug, cucumber::World)]
#[world(init = Self::custom)]
struct Generic<T: Default + Debug + 'static = usize> {
    value: T,
}
impl<T: Default + Debug + 'static> Generic<T> {
    fn custom() -> Self {
        trace("generic:init");
        Self { value: T::default() }
    }
}
#[cucumber::given(expr_js = "generic {int}", prepare_before_timeout)]
fn generic(world: &mut Generic<usize>, value: usize) {
    assert_eq!(world.value, 0);
    world.value = value;
    trace(format!("generic:{value}"));
}
#[derive(Debug, cucumber::World)]
#[world(init = Self::custom)]
struct Custom {
    value: usize,
}
impl Custom {
    fn custom() -> Self {
        trace("custom:init");
        Self { value: 41 }
    }
}
#[cucumber::given(expr_js = "custom {int}")]
fn custom(world: &mut Custom, value: usize) {
    world.value += value;
    trace(format!("custom:{}", world.value));
}
#[derive(Debug, Default, cucumber::World)]
struct Legacy;
#[cucumber::given("legacy works")]
fn legacy(_: &mut Legacy) {
    trace("legacy:body");
}
#[derive(Debug, Default)]
struct ContextWorld<T: Default + Debug + 'static> {
    value: T,
    attachments: AttachmentContext,
    completion: ExecutionControl,
}
impl<T: Default + Debug + 'static> cucumber::World for ContextWorld<T> {
    type Error = std::convert::Infallible;
    async fn new() -> Result<Self, Self::Error> {
        Ok(Self::default())
    }
    async fn new_with_runtime_context(
        context: WorldContext,
    ) -> Result<Self, Self::Error> {
        trace("contexts:init");
        Ok(Self {
            attachments: context.attachments(),
            completion: context.execution(),
            ..Self::default()
        })
    }
}
fn contextual(
    world: &mut ContextWorld<usize>,
    _: Context,
) -> LocalBoxFuture<'_, ()> {
    Box::pin(async move {
        world.value += 1;
        trace(format!("contexts:{}", world.value));
        let attachment = world.attachments.scope().unwrap();
        attachment
            .attach(Attachment::text("context payload", "text/plain"))
            .unwrap();
        let completion = world.completion.current().unwrap();
        completion.complete(Completion::Skipped).unwrap();
        *OLD_ATTACHMENT.lock().unwrap() = Some(attachment);
        *OLD_COMPLETION.lock().unwrap() = Some(completion);
    })
}
#[derive(Debug)]
struct Clock;
impl TimeoutClock for Clock {
    fn sleep(&self, duration: Duration) -> BoxFuture<'static, ()> {
        TIMERS.lock().unwrap().push(duration.as_millis());
        Box::pin(futures::future::pending())
    }
}
async fn run(directory: &Path) -> Value {
    std::fs::create_dir_all(directory).unwrap();
    let generic_source = "Feature: Generic\n Scenario: Default \
        specialization\n  Given generic 7\n";
    let generic_path = directory.join("generic.feature");
    std::fs::write(&generic_path, generic_source).unwrap();
    let generic_steps = Generic::<usize>::collection();
    let parsed =
        cucumber::gherkin::Feature::parse(generic_source, Default::default())
            .unwrap();
    let generated_metadata = generic_steps
        .find_with_options(&parsed.scenarios[0].steps[0])
        .unwrap()
        .unwrap()
        .1
        .expression_metadata()
        .is_some();
    let mut output = Vec::new();
    Generic::<usize>::cucumber()
        .steps(generic_steps)
        .with_messages(&mut output)
        .with_default_cli()
        .run(&generic_path)
        .await;
    let generic_result = json!({
    "messages":messages(output),
    "trace":take_trace(),
    "generatedExpressionMetadata":generated_metadata,

                         "inventorySpecialization":"Generic<usize>",
                             "arbitraryGenericInventory":false}
                             );
    let custom_path = directory.join("custom.feature");
    std::fs::write(
        &custom_path,
        "Feature: Custom\n Scenario: Initialization\n  Given custom 1\n",
    )
    .unwrap();
    let mut output = Vec::new();
    Custom::cucumber()
        .with_messages(&mut output)
        .with_default_cli()
        .run(&custom_path)
        .await;
    let custom_result =
        json!({"messages":messages(output),"trace":take_trace()});
    let legacy_path = directory.join("legacy.feature");
    std::fs::write(
        &legacy_path,
        "Feature: Legacy\n Scenario: Ordinary World\n  Given legacy works\n",
    )
    .unwrap();
    let mut output = Vec::new();
    Legacy::cucumber()
        .with_messages(&mut output)
        .with_default_cli()
        .run(&legacy_path)
        .await;
    let legacy_result =
        json!({"messages":messages(output),"trace":take_trace()});
    let context_source = "Feature: Context\n Scenario: Scoped evidence\n  \
        Given contextual evidence\n";
    let context_path = directory.join("contexts.feature");
    std::fs::write(&context_path, context_source).unwrap();
    let timeout = TimeoutPolicy::After(Duration::from_millis(50));
    let metadata = cucumber::support_code::RegexMetadata::new(
        "^contextual evidence$",
        vec![],
    )
    .unwrap();
    let steps = Collection::new().given_with_options(
        None,
        Regex::new("^contextual evidence$").unwrap(),
        contextual,
        DefinitionOptions::new().timeout(timeout).regular_expression(metadata),
    );
    let parsed =
        cucumber::gherkin::Feature::parse(context_source, Default::default())
            .unwrap();
    let explicit_timeout = steps
        .find_with_options(&parsed.scenarios[0].steps[0])
        .unwrap()
        .unwrap()
        .1
        .timeout_policy()
        == Some(timeout);
    let attachments = AttachmentStore::new();
    let sources = cucumber::parser::SourceStore::new();
    let support = cucumber::support_code::Store::new();
    support.publish(steps.support_code());
    let mut output = Vec::new();
    let writer = cucumber::writer::Messages::raw_with_source_store(
        &mut output,
        sources.clone(),
    )
    .with_attachment_store(attachments.clone())
    .with_support_code_store(support)
    .normalized();
    cucumber::Cucumber::new()
        .steps(steps)
        .with_attachments(attachments)
        .with_source_store(sources)
        .outcome_policy(OutcomePolicy::CucumberJs { strict_pending: true })
        .with_timeouts(
            Timeouts::default()
                .with_default(TimeoutPolicy::After(Duration::from_millis(999)))
                .with_clock(Arc::new(Clock)),
        )
        .with_writer(writer)
        .with_default_cli()
        .run(&context_path)
        .await;
    let attachment_closed = OLD_ATTACHMENT
        .lock()
        .unwrap()
        .as_ref()
        .unwrap()
        .attach(Attachment::text("must not be emitted", "text/plain"))
        == Err(cucumber::attachment::AttachmentError::ClosedScope);
    let completion_closed = OLD_COMPLETION
        .lock()
        .unwrap()
        .as_ref()
        .unwrap()
        .complete(Completion::Skipped)
        == Err(cucumber::execution::ControlError::ClosedScope);
    let contexts = json!({
    "messages":messages(output),
    "trace":take_trace(),
    "explicitTimeout":explicit_timeout,

    "timerMilliseconds":*TIMERS.lock().unwrap(),
        "attachmentClosed":attachment_closed,
        "completionClosed":completion_closed}
        );
    json!({
    "generic":generic_result,
    "custom":custom_result,
    "legacy":legacy_result,
    "contexts":contexts}
    )
}
fn main() {
    let directory =
        std::env::args().nth(1).expect("external fixture directory");
    println!("{}", futures::executor::block_on(run(Path::new(&directory))));
}
