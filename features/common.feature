# Basic check
Feature: Test the driver initialization

  Scenario: Initialize driver and load the page
    Given I load the website
    When I go to page
    Then I see this element on the page Trip.com
    And I quit driver