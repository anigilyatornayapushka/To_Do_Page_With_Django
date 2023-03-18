from typing import Any
from django.core.handlers.wsgi import (
    WSGIRequest,
)
from django.http import HttpResponse
from django.shortcuts import redirect


class IsAnonym:
    def __init__(self, get_response: Any) -> None:
        self.get_response = get_response

    def __call__(self, request: WSGIRequest) -> None:
        if request.user.is_anonymous and request.path not in ('/login/', '/reg/'):
            return redirect('/login')
        response: HttpResponse = self.get_response(request)
        return response