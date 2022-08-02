import os
import logging
import requests

from django.core.exceptions import BadRequest
from django.http import (HttpResponse, HttpResponseBadRequest)
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET", "POST"])
def webhook(request):
    times = int(os.environ.get('TIMES', 3))
    verifyToken = os.environ.get('VERIFY_TOKEN', 'DEFAULT_VERIFY_TOKEN')

    if request.method  == 'GET':
        reqChallenge = request.GET.get('hub.challenge')
        reqVerifyToken = request.GET.get('hub.verify_token')
        if verifyToken != reqVerifyToken:
            return HttpResponseBadRequest("Verify Token didn't match.")
        return HttpResponse(reqChallenge)
    
    # logging.debug("JHAO - CHECK", request.method)
    logging.info("JHAO - CHECK", request.method, verifyToken)
    # logging.error("JHAO - CHECK", request.method)
    print("JHAO - PRINT?", verifyToken)
    return HttpResponse(request.method * times)
