Feature: Login Functionality

  @loginImplemented @done
  Scenario: Login with valid credentials
    Given I navigated to Login page
    When I enter valid email address and valid password into the fields
    And I click on Login button
    Then I should get logged in

  @loginImplemented
  Scenario: Login with invalid email and valid password
    Given I navigated to Login page
    When I enter invalid email and valid password into the fields
    And I click on Login button
    Then I should get a proper warning message

  @loginImplemented
  Scenario: Login with valid email and invalid password
    Given I navigated to Login page
    When I enter valid email and invalid password into the fields
    And I click on Login button
    Then I should get a proper warning message

  @loginImplemented
  Scenario: Login with invalid credentials
    Given I navigated to Login page
    When I enter invalid email and invalid password into the fields
    And I click on Login button
    Then I should get a proper warning message

  @loginImplemented
  Scenario: Login without entering any credentials
    Given I navigated to Login page
    When I dont enter anything into email and password fields
    And I click on Login button
    Then I should get a proper warning message