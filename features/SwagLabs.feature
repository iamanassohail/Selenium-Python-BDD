Feature: Automation for Swag Labs

  Scenario: Login with valid credentials
    Given Go to Url
    When enter valid username
    And enter valid password
    And click sign in
    Then assert user land to the dashboard

  Scenario: Sort the item from low to high
    Given go to Dashboard
    When select the prize low to high
    Then verify items are sort in low to high
    When add lowest two items in the cart
    And go to the cart
    Then assert the quantity and total items in cart with prices