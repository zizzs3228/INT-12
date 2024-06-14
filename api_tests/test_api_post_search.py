import requests
import allure
import json
from conftest import BASE_URL


@allure.feature('UI Tests')
@allure.story('User Registration')
def test_api_get_brands():
    r = requests.post(BASE_URL+'/api/searchProduct')
    assert r.status_code == 200
    from_json = json.loads(r.text)
    assert from_json
    assert from_json['message']
    assert from_json['message']=="Bad request, search_product parameter is missing in POST request."