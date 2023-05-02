import requests
from services.dm_api_account import DmApiAccount


def test_post_v1_account_login():
    api = DmApiAccount(host='http://localhost:5051')
    json = {
        "login": "login22",
        "password": "1213456789",
        "rememberMe": False
    }
    response = api.login.post_v1_account_login(
        json=json
    )

    print(response)
