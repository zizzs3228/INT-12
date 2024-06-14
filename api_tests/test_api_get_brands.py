import requests
import allure
import json
from conftest import BASE_URL

brands = [{"id": 1, "brand": "Polo"}, {"id": 2, "brand": "H&M"}, {"id": 3, "brand": "Madame"}, {"id": 4, "brand": "Madame"}, {"id": 5, "brand": "Mast & Harbour"}, {"id": 6, "brand": "H&M"}, {"id": 7, "brand": "Madame"}, {"id": 8, "brand": "Polo"}, {"id": 11, "brand": "Babyhug"}, {"id": 12, "brand": "Babyhug"}, {"id": 13, "brand": "Allen Solly Junior"}, {"id": 14, "brand": "Kookie Kids"}, {"id": 15, "brand": "Babyhug"}, {"id": 16, "brand": "Babyhug"}, {"id": 18, "brand": "Kookie Kids"}, {"id": 19, "brand": "Allen Solly Junior"}, {"id": 20, "brand": "Kookie Kids"}, {"id": 21, "brand": "Biba"}, {"id": 22, "brand": "Biba"}, {"id": 23, "brand": "Biba"}, {"id": 24, "brand": "Allen Solly Junior"}, {"id": 28, "brand": "H&M"}, {"id": 29, "brand": "Polo"}, {"id": 30, "brand": "Polo"}, {"id": 31, "brand": "H&M"}, {"id": 33, "brand": "Polo"}, {"id": 35, "brand": "H&M"}, {"id": 37, "brand": "Polo"}, {"id": 38, "brand": "Madame"}, {"id": 39, "brand": "Biba"}, {"id": 40, "brand": "Biba"}, {"id": 41, "brand": "Madame"}, {"id": 42, "brand": "Mast & Harbour"}, {"id": 43, "brand": "Mast & Harbour"}]

@allure.feature('API Tests')
@allure.story('Get brands')
def test_api_get_brands():
    r = requests.get(BASE_URL+'/api/brandsList')
    assert r.status_code == 200
    from_json = json.loads(r.text)
    assert from_json
    assert from_json['brands']
    assert from_json['brands']==brands