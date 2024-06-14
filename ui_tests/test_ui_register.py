import allure
from conftest import BASE_URL


@allure.feature('UI Tests')
@allure.story('User Registration')
def test_ui_register(page,email,password):
    page.goto(BASE_URL+'/login')
    page.fill('form[action="/signup"] input[data-qa="signup-name"]', 'TestUser')
    page.fill('form[action="/signup"] input[data-qa="signup-email"]', email)
    page.click('button[data-qa="signup-button"]')
    page.click('input[id="id_gender1"]')
    page.fill('form[action="/signup"] input[data-qa="password"]', password)
    page.select_option('select[data-qa="days"]','10')
    page.select_option('select[data-qa="months"]','March')
    page.select_option('select[data-qa="years"]','2009')
    page.fill('input[data-qa="first_name"]','Egor')
    page.fill('input[data-qa="last_name"]','Vasilyevich')
    page.fill('input[data-qa="company"]','ITMO')
    page.fill('input[data-qa="address"]','ksadfjg, lksdjfgsl, kdfjg')
    page.select_option('select[id="country"]','Israel')
    page.fill('input[id="state"]','Bruhm')
    page.fill('input[id="city"]','Bruhm-city')
    page.fill('input[id="zipcode"]','579899')
    page.fill('input[id="mobile_number"]','+79116666666')
    page.click('button[type="submit"]')
    assert page.locator('b', has_text='Account Created').is_visible()