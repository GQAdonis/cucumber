Feature: Real evidence
  Scenario: Actual operation
    Given observe pass
    Then check the observation
  Scenario: Unmapped failure
    Given observe fail
    Then check the observation
