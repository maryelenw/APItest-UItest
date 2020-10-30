# API Automation

This is an automation test using Selenium, Python and Behave (Cucumber). It provides the following automated tests for the API.

API Test Feature:

- Validate connection with the API
- Validate request and response for entry with valid parameters
- Validate request and response for entry with invalid parameters
  - state not registered
  - empty fields

UI Test Feature:
  - Access Demo Cart website and complete an order

I used Linux Mint environment to develop this automation.


**Prerequisites**

- Python 3.6 or above
- Pip
- Behave
- Selenium

**Installation Guide**

If you use linux you can just type those commands and go to Step 3:

- `sudo apt install python3 python3-pip python3-behave`
- `pip3 install -r requirements.txt`

If you not, you have the follow the downloads the steps:

**_Step 1:_** Download and Install the latest version of Python on the official site: https://www.python.org/downloads/

You can find Installation Guide to your system here: https://realpython.com/installing-python/

**_Step 2:_** Install or Update pip

You can find Installation Guide to your system here: https://pypi.org/project/pip/

**_Step 3:_** Install behave and all dependencies listed on requirements.txt inside your project
Execute the command line:

- `pip install -r requirements.txt` or
- `pip3 install -r requirements.txt`

**_Step 4:_** Install Selenium and the appropriate webdrivers

You can find an installation Guide here: https://selenium-python.readthedocs.io/installation.html

**_Step 5:_** To run the test cases you can run:

- `behave`
- `behave -n 'the scenario you want to run'`
- `behave ./features/test_you_want.feature`
