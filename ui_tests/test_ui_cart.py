import allure
from conftest import BASE_URL

@allure.feature('UI Tests')
@allure.story('User Registration')
def test_ui_register_login(page):
    page.goto(BASE_URL+'/view_cart')
    assert page.locator('b', has_text='Cart is empty!').is_visible()
    page.goto(BASE_URL+'/products')
    page.click('a[data-product-id="2"]')
    page.wait_for_timeout(1000)
    page.goto(BASE_URL+'/view_cart')
    page.wait_for_timeout(1000)
    assert page.locator('a[href="/product_details/2"]').is_visible()
    page.click('a[class="cart_quantity_delete"]')
    page.wait_for_timeout(500)
    assert page.locator('b', has_text='Cart is empty!').is_visible()