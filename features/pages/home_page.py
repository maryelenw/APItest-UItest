from features.pages.base_page import BasePage


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
    }