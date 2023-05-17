from django.http import JsonResponse
from rest_framework import status
from rest_framework.exceptions import APIException


class BaseCustomException(APIException):
    detail = None
    status_code = None

    def __init__(self, detail, code):
        super().__init__(detail, code)
        self.detail = detail
        self.status_code = code


def error_404(request, exception):
    data = {
        'message': 'Endpoint Not Found',
        'path': request.path,
        'status_code': 404

        }
    response =  JsonResponse(data=data)
    return response


def error_500(request):
    data = {
        'message': 'Internal Server Error',
        'status_code': 500  }
    response =  JsonResponse(data=data)
    return response