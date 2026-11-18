@docs
Feature: Readers can use clearly attributed fork documentation
  The published capabilities must be distinguishable from planned SDK work.
  A local production build must work without changing existing release workflows.

  Scenario Outline: Read the fork identity and current implementation status
    Given the production documentation for "<project>" is served below a non-root path
    When a reader opens the home page
    Then the page identifies the GQAdonis fork without upstream endorsement
    And the reader can open the compatibility and evidence pages
    And no local asset request or browser runtime error has failed
    Examples:
      | project  |
      | cucumber |
      | gherkin  |

  Scenario Outline: Follow a permanent getting-started link on a phone
    Given the production documentation for "<project>" is served below a non-root path
    When a reader opens the getting-started deep link with a phone viewport
    Then the page explains a pinned checkout instead of an unpublished registry release
    And the getting-started page has no horizontal overflow
    And the navigation is usable with the keyboard
    And the page has no horizontal overflow
    Examples:
      | project  |
      | cucumber |
      | gherkin  |

  Scenario: Distinguish SDK research from executable packages
    Given the production documentation for "cucumber" is served below a non-root path
    When a reader opens the SDK page
    Then both Behave and pytest-bdd are identified as unverified adapter tracks
    And the page does not offer an npm or Python package installation as available

  Scenario Outline: Recover from a missing documentation page
    Given the production documentation for "<project>" is served below a non-root path
    When a reader opens an unknown documentation path
    Then the built not-found page is shown with a route back to the fork documentation
    Examples:
      | project  |
      | cucumber |
      | gherkin  |

  @negative
  Scenario Outline: Refuse a broken internal link before hosting
    Given an isolated copy of the "<project>" documentation source
    When an author adds an internal link to a missing page
    Then the same production build fails and identifies the missing route
    And the original source and build remain unchanged
    Examples:
      | project  |
      | cucumber |
      | gherkin  |

  @negative
  Scenario: Refuse to overwrite retained verification artifacts
    Given an evidence directory already contains preserved artifact bytes
    When the documentation boundary is launched with that directory
    Then it refuses before starting another scenario run
    And all preserved artifact bytes remain unchanged
