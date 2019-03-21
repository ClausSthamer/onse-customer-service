Feature: Update customer name

  Scenario: Update the name of a customer
    Given customer "Nicole Forsgren" with ID "12345" exists
    When I update customer "12345" name to "Nicole Smith"
    Then I should fetch customer "Nicole Smith" with customer ID "12345"
