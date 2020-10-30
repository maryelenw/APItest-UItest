from behave import *
from nose.tools import assert_equals
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from features.object import Singleton
from features.pages.home_page import HomePage
from selenium.webdriver.common.keys import Keys
import time

@given(u'I search for a new product')
def search_product(context):
  home_page = Singleton.getInstance(context,HomePage)
  context.browser.get(home_page.project_url)
  search_field = context.browser.find_element(By.CLASS_NAME, home_page.locators['search_field']) 
  search_field.send_keys('t-shirt black', Keys.ENTER)

@given(u'I access this product on the table grid')
def access_table_grid(context):
  home_page = Singleton.getInstance(context,HomePage)
  found_product = context.browser.find_element(By.CLASS_NAME, home_page.locators['found_product'])
  found_product.click()

@then(u'I add this product to the cart')
def add_product_cart(context):
    home_page = Singleton.getInstance(context,HomePage)
    context.browser.find_element(By.ID, home_page.locators['admin_banner']).click()
    add_cart_button = context.browser.find_element(By.ID, home_page.locators['add_cart_button'])
    add_cart_button.click()

@then(u'I check the item on the cart and total price')
def check_product_price(context):
    home_page = Singleton.getInstance(context,HomePage)
    context.browser.find_element(By.CLASS_NAME, home_page.locators['product_description'])
    context.browser.find_element(By.ID, home_page.locators['product_price'])
    
@then(u'I do the Checkout')
def checkout(context):
    home_page = Singleton.getInstance(context,HomePage)
    WebDriverWait(context.browser, 100).until(EC.invisibility_of_element((By.XPATH, "//*[contains(text(), 'The product was added to your cart')]")))
    WebDriverWait(context.browser, 100).until(EC.element_to_be_clickable((By.ID, home_page.locators['cart_status']))).click()
    checkout = context.browser.find_element_by_xpath("//*[contains(text(), 'Checkout')]")
    checkout.click()

@then(u'I select the “Phone Order” Payment')
def phone_order(context):
    home_page = Singleton.getInstance(context,HomePage)
    phone_ordering = context.browser.find_element(By.ID, home_page.locators['phone_ordering'])
    phone_ordering.click()
  
@then(u'I proceed with the order')
def procees_order(context):
    home_page = HomePage(context)
    home_page.fill_in_Product()

    
    
    
