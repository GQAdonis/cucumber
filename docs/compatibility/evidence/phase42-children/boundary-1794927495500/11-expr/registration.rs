use cucumber::{given, then, World as _};
use std::{convert::Infallible, str::FromStr};
#[derive(Debug, Default, cucumber::World)]
struct Registration { seen: bool }
#[derive(Debug, cucumber::Parameter)]
#[param(name = "dotted.name", regex = "value")]
struct Native(String);
impl FromStr for Native {
    type Err = Infallible;
    fn from_str(value: &str) -> Result<Self, Self::Err> { Ok(Self(value.to_owned())) }
}
#[given(expr = "value {dotted.name}")]
fn accept_value(world: &mut Registration, value: Native) {
    assert_eq!(value.0, "value", "actual custom handler value");
    world.seen = true;
    println!("PHASE42_ACTUAL_HANDLER_VALUE=value");
}
#[then("the actual handler executed")]
fn observed(world: &mut Registration) { assert!(world.seen); }
#[tokio::main(flavor = "current_thread")]
async fn main() {
    Registration::cucumber().with_default_cli().fail_on_skipped()
        .run_and_exit("registration.feature").await;
}
