import requests
from services.dm_api_account import Facade


def test_post_v1_account_login():
    api = Facade(host='http://localhost:5051')
    json = {
        "login": "login22",
        "password": "1213456789",
        "rememberMe": False
    }
    response = api.login_api.post_v1_account_login(
        json=json
    )

    print(response)
