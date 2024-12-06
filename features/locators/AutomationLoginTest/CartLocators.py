class CartLocator:
    cart_table_xpath = "//*[@class='container-fluid cart-info product-list']/table"
    cart_nav_button_xpath = "(//li[@data-id='menu_cart'])[1]"
    total_amount_span_xpath = "//*[@class='bold totalamout']"
    update_cart_button_id = "cart_update"