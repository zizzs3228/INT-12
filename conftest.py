import pytest
from playwright.sync_api import sync_playwright
import random
import string

BASE_URL = 'https://www.automationexercise.com'

@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def browser(playwright_instance):
    browser = playwright_instance.chromium.launch(headless=False)
    yield browser
    browser.close()
    
@pytest.fixture(scope="function")
def page(browser):
    page = browser.new_page()
    yield page
    page.close()
    
@pytest.fixture(scope='session')
def email():
    length=15
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    yield random_string+'@mail.ru'

@pytest.fixture(scope='session')
def password():
    length=15
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    yield random_string