# from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# use_step_matcher('re')
browser = webdriver.Chrome(ChromeDriverManager().install())
# @given('I am on the homepage')
def step_impl():
    browser.get('http://127.0.0.1:5000')
    print(browser)
    print(type(browser))

step_impl()