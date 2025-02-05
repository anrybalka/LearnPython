import requests
import pytest

def test_status_code():
    response = requests.get('https://petstore.swagger.io/v2/store/inventory', verify=False)
    assert response.status_code == 200


def test_is_response_has_body():
    response = requests.get('https://petstore.swagger.io/v2/pet/10997', verify=False)
    jresp = response.json()
    assert jresp["id"] == 10997

