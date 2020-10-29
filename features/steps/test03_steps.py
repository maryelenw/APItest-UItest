from behave import *
from nose.tools import assert_equals
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import requests
import time

@given(u'I sent a request for the API without fill the fields')
def create_request(context):
  request = requests.get('https://api.interzoid.com/getweather?license=0494cb1205c26055257bf6fad3e29873&city= &state= ')
  print(request.text)
  assert(request.status_code == 400)

@then(u'I validate the response from the request')
def validate_response(context):
  response = requests.get('https://api.interzoid.com/getweather?license=0494cb1205c26055257bf6fad3e29873&city= &state= ')
  print(response.content) 
  data = response.text
  assert_equals('Insufficient parameters: city and state are required\n', data)