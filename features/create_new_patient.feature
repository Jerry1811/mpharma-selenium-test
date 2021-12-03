Feature: Creation of new patient

  Scenario: Creating a new patient successfully
    Given patient management system homepage is displayed
    When the user enters their firstname
    And enter their middle name
    And enter their lastname
    And enter phone number
    And enter valid date of birth
    And enter address
    And click on add new user button
    Then the user should be added to the system
    And close browser
