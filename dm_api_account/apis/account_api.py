from requests import Response
from restclient.restclient import Restclient
from ..models import *
from dm_api_account.models.user_envelope_model import UserEnvelop


class AccountApi:
    def __init__(self, host, headers=None):
        self.host = host
        self.client = Restclient(host=host, headers=headers)
        if headers:
            self.client.session.heasers.update(headers)

    def post_v1_account(self, json: Registration, **kwargs) -> Response:
        """
        :param json registration_model
        Register new user
        :return:
        """

        response = self.client.post(
            path=f"/v1/account",
            json=json.dict(by_alias=True, exclude_none=True),
            **kwargs
        )
        return response

    def post_v1_account_password(self, json: ResetPassword, **kwargs) -> Response:
        """
        :param json reset_password_model
        Reset registered user password
        :return:
        """

        response = self.client.post(
            path=f"/v1/account/password",
            json=json.dict(by_alias=True, exclude_none=True),
            **kwargs
        )
        return response

    def put_v1_account_email(self, json: ChangeEmail, **kwargs) -> Response:
        """
        :param json change_email_model
        Change registered user email
        :return:
        """

        response = self.client.put(
            path=f"/v1/account/email",
            json=json.dict(by_alias=True, exclude_none=True),
            **kwargs
        )
        return response

    def put_v1_account_password(self, json: ChangePassword, **kwargs) -> Response:
        """
        :param json: change_password_model
        Change registered user password
        :return:
        """

        response = self.client.put(
            path=f"/v1/account/password",
            json=json.dict(by_alias=True, exclude_none=True),
            **kwargs
        )
        return response

    def put_v1_account_token(self, token: str, **kwargs) -> Response:
        """
        Activate registered user
        :return:
        """

        response = self.client.put(
            path=f"/v1/account/{token}",
            **kwargs
        )
        UserEnvelop(**response.json())
        return response

    def get_v1_account(self, **kwargs) -> Response:
        """
        Get current user
        :return:
        """

        response = self.client.get(
            path=f"/v1/account",
            **kwargs
        )
        return response
