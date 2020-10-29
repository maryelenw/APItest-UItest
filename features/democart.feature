Feature: Access X website and complete a purchase

  Scenario: Access site and do all the steps to buy a product
    Given I search for a new product
    And I access this product on the table grid
    Then I add this product to the cart
    And I check the item on the cart and total price
    Then I do the Checkout
    And I select the “Phone Order” Payment
    Then I proceed with the order
