import os
import logging
import requests

from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

@require_http_methods(["POST"])
def webhook(request):
    times = int(os.environ.get('TIMES', 3))
    verifyToken = os.environ.get('VERIFY_TOKEN', 'DEFAULT_VERIFY_TOKEN')

    # logging.debug("JHAO - CHECK", request.method)
    logging.info("JHAO - CHECK", request.method, verifyToken)
    # logging.error("JHAO - CHECK", request.method)
    print("JHAO - PRINT?", verifyToken)
    return HttpResponse(request.method * times)
