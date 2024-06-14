import allure
from conftest import BASE_URL

@allure.feature('UI Tests')
@allure.story('Adding review')
def test_ui_register_login(page):
    page.goto(BASE_URL)
    page.click('a[href="/product_details/2"]')
    page.fill('form input[id="name"]','SashaMasha')
    page.fill('form input[id="email"]','SashaMasha@mail.ru')
    page.fill('form textarea','l;aksdjf;alksdjfa;lksdfja;lskdfja;lsdkfja;lskdfj')
    page.click('form button[type="submit"]')
    page.wait_for_timeout(300)
    assert page.locator('span', has_text='Thank you for your review.').is_visible()
    