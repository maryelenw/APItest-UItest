from behave import *
from nose.tools import assert_equals
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import requests
import time

@given(u'I sent a request for the API informing a city, state')
def create_request(context):
  request = requests.get('https://api.interzoid.com/getweather?license=154b4435a1d20ec20f5c9c4848459899&city=Round%20Rock&state=TX')
  print(request.text)
  assert request.status_code == 200  
  if request.status_code == 200:
    data = request.json()
    print(data["City"])
    

@then(u'I validate the response code')
def validate_response(context):
  response = requests.get('https://api.interzoid.com/getweather?license=154b4435a1d20ec20f5c9c4848459899&city=Round%20Rock&state=TX')
  print(response.text)
  assert response.status_code == 200  
  data = response.json()
  print(data["State"])


