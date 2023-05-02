import requests
import json

from services.dm_api_account import DmApiAccount


def test_put_v1_account_email():
    api = DmApiAccount(host='http://localhost:5051')
    json = {
        "login": "login_1",
        "password": "Login_11",
        "email": "asdasd@gmail.com"
    }
    response = api.account.put_v1_account_email(
        json=json
    )

    print(response)
