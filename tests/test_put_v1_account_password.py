import requests
import json
from services.dm_api_account import Facade


def test_put_v1_account_password():
    api = Facade(host='http://localhost:5051')
    json = {
        "login": "login_2",
        "token": "asdasd",
        "oldPassword": "oldpasslog",
        "newPassword": "newpasslog"
    }
    response = api.account_api.put_v1_account_password(
        json=json
    )

    print(response)
