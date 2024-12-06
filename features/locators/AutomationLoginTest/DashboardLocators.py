from utilities import ConfigReader

class DashboardLocators:
    item_count = 0
    total_amount = 0.00
    url = ConfigReader.read_configuration("AutomationTestStore", "url")
    lgon_register_button_id = "customer_menu_top"
    currency_dropdown_class = "language"
    euro_option_xpath = "//a[contains(text(),'€ Euro')]"
    catagory_menu_nav_xpath = "//*[@id='categorymenu']/nav/ul/li"
    items_grid_xpath = "//div[@class='thumbnails grid row list-inline']"
    items_cart_xpath = "//div[@class='thumbnails grid row list-inline']/div/div[@class='thumbnail']"
    sale_tag_span_class = "sale"
    out_of_stock_button_class = "nostock"
    add_to_cart_button_class = "productcart"
    new_price_dev_class = "pricenew"
    dollar_option_xpath = "//a[contains(text(),'$ US Dollar')]"