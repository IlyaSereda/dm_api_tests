import requests
from services.dm_api_account import DmApiAccount


def test_post_v1_account():
    api = DmApiAccount(host='http://localhost:5051')
    json = {
        "login": "login_5",
        "email": "login5@gmail.com",
        "password": "login_5"
    }
    response = api.account.post_v1_account(
        json=json
    )

    print(response)