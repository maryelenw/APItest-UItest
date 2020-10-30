from features.pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time


class HomePage(BasePage):

    project_url = "http://demo.cs-cart.com"

    locators = {
    "search_field":"ty-search-block__input",
    "found_product":"cm-item-gallery",
    "add_cart_button":"button_cart_38",
    "product_price":"sec_price_456910969",
    "product_description": "ty-product-notification__product-name",
    "cart_status": "cart_status_8",
    "checkout":"Checkout",
    "admin_banner":"bp_off_bottom_panel",
    "phone_ordering":"payments_2",
    "customer_phone":"customer_phone",
    "customer_city":"litecheckout_city",
    "customer_address":"litecheckout_s_address",
    "customer-zip_code":"litecheckout_s_zipcode",
    "customer_full_name":"litecheckout_fullname",
    "customer_phone":"litecheckout_phone",
    "customer_email":"litecheckout_email",
    "customer_note": "litecheckout_comment_to_shipping",
    "check_accept_terms":"Select this check box to accept the",
    "im_not_a_robot": "recaptcha-anchor",
    "place_order":"litecheckout_place_order",
    "product_added": "The product was added to your cart",
    }

    def fill_in_Product(self):
        customer_city = self.browser.find_element(By.ID, self.locators['customer_city'])
        customer_city.send_keys("Boston")
        customer_address = self.browser.find_element(By.ID, self.locators['customer_address'])
        customer_address.send_keys("alfeneiros four street")
        customer_full_name = self.browser.find_element(By.ID, self.locators['customer_full_name'])
        customer_full_name.send_keys("Test")
        customer_phone = self.browser.find_element(By.ID, self.locators['customer_phone'])
        customer_phone.send_keys("48998098738")
        customer_email = self.browser.find_element(By.ID, self.locators['customer_email'])
        customer_email.send_keys("test@test.com")
        customer_note = self.browser.find_element(By.ID, self.locators['customer_note'])
        customer_note.send_keys("note 1")
        self.browser.find_element(By.ID, self.locators['admin_banner']).click()
        self.browser.find_element_by_xpath("//*[contains(text(), 'Select this check box to accept the ')]").click()

