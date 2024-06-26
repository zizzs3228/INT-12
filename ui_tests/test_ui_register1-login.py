import allure
from conftest import BASE_URL

@allure.feature('UI Tests')
@allure.story('User login')
def test_ui_register_login(page,email,password):
    page.goto(BASE_URL+'/logout')
    page.goto(BASE_URL+'/login')
    page.fill('form[action="/login"] input[name="email"]',email)
    page.fill('form[action="/login"] input[name="password"]',password)
    page.click('form[action="/login"] button')
    assert page.locator('a',has_text="Logged in as").is_visible()