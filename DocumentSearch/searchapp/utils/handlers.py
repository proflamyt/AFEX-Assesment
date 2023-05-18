from rest_framework.views import exception_handler
from rest_framework import status

from core.utils.views import BaseCustomException

def custom_exception_handler(exc, context):

    response = exception_handler(exc, context)
    
    if response is not None:
        response.data['status_code'] = response.status_code

    return response


class ConnectionErrorException(BaseCustomException):

    def __init__(self, detail):
        super().__init__(detail, status.HTTP_503_SERVICE_UNAVAILABLE)