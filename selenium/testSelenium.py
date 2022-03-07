# from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# use_step_matcher('re')

# @given('I am on the homepage')
def step_impl():
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get('http://127.0.0.1:8000')

# @then('I am on the blog page')
def step_then():
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get('http://127.0.0.1:8000')
    link = browser.find_element_by_id('blog-link')
    link.click()
    expected_url = 'http://127.0.0.1:8000/blog'
    assert browser.current_url == expected_url, "It doesn't stay in the correct url"

step_impl()
step_then()