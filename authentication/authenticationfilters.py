from datetime import datetime

import jwt
from django.conf import settings
from rest_framework import authentication, exceptions

from authentication.models import User
from ping.exceptions import AccessTokenExpired
from split_expenses_app_backend.settings import ACCESS_TOKEN_EXPIRATION_TIME
from utils.datetransformations import default_date_format


class JWTAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        auth_data = authentication.get_authorization_header(request)

        if not auth_data:
            return None

        token = auth_data.decode('utf-8')

        try:
            payload = jwt.decode(token, settings.JWT_SECRET_KEY)
            token_create_date_string = payload['create_date']
            token_create_date = datetime.strptime(token_create_date_string, default_date_format)
            if (datetime.now() - token_create_date).seconds > ACCESS_TOKEN_EXPIRATION_TIME:
                raise AccessTokenExpired()
            user = User.objects.get(username=payload['username'])
            return user, token

        except jwt.DecodeError as identifier:
            raise exceptions.AuthenticationFailed(
                'Your token is invalid,login')
        except jwt.ExpiredSignatureError as identifier:
            raise exceptions.AuthenticationFailed(
                'Your token is expired,login')
