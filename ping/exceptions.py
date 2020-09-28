from rest_framework import status
from rest_framework.exceptions import APIException


class AccessTokenExpired(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = ('Access Token Expired.')
    default_code = 'authentication_failed'

