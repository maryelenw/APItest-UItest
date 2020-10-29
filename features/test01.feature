Feature: Sending correct data to API

  Scenario: Informing a correct city and state in the API request
    Given I sent a request for the API informing a city, state
    Then I validate the response code
  