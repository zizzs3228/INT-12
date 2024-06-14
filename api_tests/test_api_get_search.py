import requests
import allure
import json
from conftest import BASE_URL


@allure.feature('API Tests')
@allure.story('Get search')
def test_api_get_brands():
    r = requests.get(BASE_URL+'/api/searchProduct')
    assert r.status_code == 200
    from_json = json.loads(r.text)
    assert from_json
    assert from_json['message']
    assert from_json['message']=="This request method is not supported."