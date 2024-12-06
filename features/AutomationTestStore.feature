Feature: Automation for Automation Test Store

  @done
  Scenario: Login to Automation Test Store and add item in cart and calculate price and count of items
    Given Goto Automation Test Store
    When Login to the Website
    And Select the currency to euro
    And From each section select all sales items and add it into the cart
    Then Go to the AutoTestStore cart then assert the items count and amount
    When Delete items until amount less then 200 Euro
    And Change currancy to dollor
    And Delete items until amount less then 200 Dollar
