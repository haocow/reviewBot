import json
import logging
import os
import requests

from django.core.exceptions import BadRequest
from django.http import (HttpResponse, HttpResponseForbidden)
from django.views.decorators.http import require_http_methods
from hashlib import sha256
from utils import haoPrint

@require_http_methods(["GET", "POST"])
def webhook(request):
    times = int(os.environ.get('TIMES', 3))
    verifyToken = os.environ.get('VERIFY_TOKEN', 'DEFAULT_VERIFY_TOKEN')

    if request.method  == 'GET':
        reqChallenge = request.GET.get('hub.challenge')
        reqMode = request.GET.get('hub.mode')
        reqVerifyToken = request.GET.get('hub.verify_token')
        if "subscribe" == reqMode and verifyToken == reqVerifyToken:
            return HttpResponse(reqChallenge)
        logging.warn("Challenge failed in request.")
        return HttpResponseForbidden()
    else:
        try:
            verifySignature(request)
        except Exception as e:
            logging.warn(str(e))
            return HttpResponseForbidden()
        reqBodyStr = request.body
        reqBodyObj = json.loads(reqBodyStr)

        haoPrint("JHAO - PRINT?", reqBodyObj)
        return HttpResponse(request.method * times)

def verifySignature(request):
    reqSignature = request.headers['x-hub-signature']
    if reqSignature is None:
        logging.warn("Missing x-hub-signature in headers.")
    else:
        signatureHash = reqSignature.split("=")[1]
        expectedHash = sha256(str.encode(os.environ.get('APP_SECRET'))).hexdigest()
        haoPrint(signatureHash, expectedHash)
        if signatureHash != expectedHash:
            logging.warn("Couldn't validate the request signature.")
            # raise Exception("Couldn't validate the request signature.")

