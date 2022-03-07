# from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
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


def step_blog_page():
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get('http://127.0.0.1:8000/blog')
    link = browser.find_element_by_id('home-link')
    link.click()
    expected_url = 'http://127.0.0.1:8000/'
    assert browser.current_url == expected_url, f"It doesn't stay in the correct url, stay in {browser.current_url}"

def step_content(tag, content):
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get('http://127.0.0.1:8000')
    title_tag = browser.find_element(By.TAG_NAME, tag)
    assert title_tag.is_displayed() 
    assert title_tag.text == content

def step_locations():
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get('http://127.0.0.1:8000/post')
    browser.get('http://127.0.0.1:8000/blog')
    browser.get('http://127.0.0.1:8000/')
    
step_impl()
step_then()
step_blog_page()
step_content('h1', 'This is the homepage')