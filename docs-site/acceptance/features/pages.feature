@pages
Feature: Readers can reach the verified fork documentation from GitHub
  Documentation deployment is independent of Rust and registry releases.
  Run this boundary only after both Pages deployments and About links are ready.

  Scenario Outline: Open public documentation and its permanent routes
    Given the successful Pages deployment for "<project>" is available
    When a reader opens its public home and getting-started deep link
    Then both pages identify the independent GQAdonis fork
    And the public pages load their local assets without browser errors
    Examples:
      | project  |
      | cucumber |
      | gherkin  |

  Scenario Outline: Discover the deployed site from the repository About link
    Given the successful Pages deployment for "<project>" is available
    When a reader follows the repository About website
    Then it points to the same HTTPS Pages site and serves the fork documentation
    Examples:
      | project  |
      | cucumber |
      | gherkin  |
