Feature: Sending a request with empty fields to API 

  Scenario: Sending empty fields to API
    Given I sent a request for the API without fill the fields
    Then I validate the response from the request