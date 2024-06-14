import allure
from conftest import BASE_URL


@allure.feature('UI Tests')
@allure.story('Scroll down + arrow up')
def test_ui_scroll_down(page):
    page.goto(BASE_URL)
    page.evaluate("""
        window.scrollTo(0, document.body.scrollHeight);
    """)
    page.wait_for_timeout(1000)
    assert page.locator('h2', has_text='Subscription').is_visible()
    page.click('a[id="scrollUp"]')
    page.wait_for_timeout(1000)
    assert page.locator('a', has_text='Home').is_visible()