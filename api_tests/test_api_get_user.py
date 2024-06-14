import requests
import allure
import json
from conftest import BASE_URL


@allure.feature('UI Tests')
@allure.story('User Registration')
def test_api_get_brands():
    data = {'email': 'asdfasdf@mail.com', 'password':'asdfasdfasdf'}
    r = requests.post(BASE_URL+'/api/verifyLogin',data=data)
    from_json = json.loads(r.text)
    assert from_json
    assert from_json['message']
    assert from_json['message']=="User not found!"
    