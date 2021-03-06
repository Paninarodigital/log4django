from django.http import HttpResponse
from django.utils.importlib import import_module
from django.conf import settings

from .settings import AUTHENTICATION_PIPELINE


class Log4DjangoAuthenticationMiddleware(object):

    def process_request(self, request):
        if not settings.DEBUG:
            status = False
            for pipeline in AUTHENTICATION_PIPELINE:
                module_str, authenticator_str = pipeline.rsplit('.', 1)
                module = import_module(module_str)
                authenticator = getattr(module, authenticator_str)
                if authenticator(request):
                    status = True
            if not status:
                return HttpResponse('Unauthorized', status=401)
