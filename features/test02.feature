Feature: Sending incorrect data to API

  Scenario: Informing an incorrect state in the API post
    Given I sent a request for the API informing a wrong state
    Then I validate the description from the bad request
  