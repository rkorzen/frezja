from django.utils.translation import activate
from django.conf import settings


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print("request:", request)
        # set_language(request, "en")
        response = self.get_response(request)

        print("response:", response)
        # Code to be executed for each request/response after
        # the view is called.

        return response



