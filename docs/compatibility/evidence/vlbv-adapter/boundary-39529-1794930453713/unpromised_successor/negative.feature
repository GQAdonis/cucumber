Feature: Oracle sensitivity
  Scenario: Plausible wrong observation
    Given observe fail
    Then check the observation
