import requests
from services.dm_api_account import DmApiAccount
from services.mailhog import MailhogApi
import structlog


structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]

)
def test_post_v1_account():
    mailhog = MailhogApi(host='http://localhost:5025')
    api = DmApiAccount(host='http://localhost:5051')
    json = {
        "login": "login_12",
        "email": "login12@gmail.com",
        "password": "login_12"
    }
    response = api.account.post_v1_account(json=json)
    assert response.status_code == 201, f'Status code should be 201 but: {response.status_code}'
    token = mailhog.get_token_from_last_email()
    response = api.account.put_v1_account_token(token=token)
