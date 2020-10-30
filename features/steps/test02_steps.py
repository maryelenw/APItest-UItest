from behave import *
from nose.tools import assert_equals
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import requests
import time

@given(u'I sent a request for the API informing a wrong state')
def create_request(context):
  request = requests.get('https://api.interzoid.com/getweather?license=154b4435a1d20ec20f5c9c4848459899&city=Tampa&state=TX')

@then(u'I validate the description from the bad request')
def validate_response(context):
  response = requests.get('https://api.interzoid.com/getweather?license=154b4435a1d20ec20f5c9c4848459899&city=Tampa&state=TX')
  data = response.text
  assert(response.status_code == 404)
  assert_equals("City and state location not found\n", data)