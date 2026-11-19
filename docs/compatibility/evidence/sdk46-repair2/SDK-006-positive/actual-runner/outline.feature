Feature: Rows
 Rule: resources
  Scenario Outline: result <outcome>
   Given <outcome>
   Examples: selected
    | outcome |
    | fail |
    | pass |
    | fail |
    | excluded |
