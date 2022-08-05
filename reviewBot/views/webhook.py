import json
import logging
import os

from django.http import (HttpResponse, HttpResponseForbidden)
from django.views.decorators.http import require_http_methods
from reviewBot.utils.constants import YOURE_WELCOME_MESSAGE_TEXT
from reviewBot.utils.messages import containsThanks, isReviewRequestReply, sendMessageToUser
from reviewBot.utils.print import haoPrint

@require_http_methods(["GET", "POST"])
def webhook(request):
    if request.method  == 'GET':
        verifyToken = os.environ.get('VERIFY_TOKEN')

        reqChallenge = request.GET.get('hub.challenge')
        reqMode = request.GET.get('hub.mode')
        reqVerifyToken = request.GET.get('hub.verify_token')

        if "subscribe" == reqMode and verifyToken == reqVerifyToken:
            return HttpResponse(reqChallenge)
        logging.warn("Challenge failed in request.")
        return HttpResponseForbidden()
    else:
        # TODO: add signature verification
        reqBodyStr = request.body
        reqBodyObj = json.loads(reqBodyStr)
        reqObject = reqBodyObj["object"]
        reqEntry = reqBodyObj["entry"][0]
        reqMessaging = reqEntry["messaging"][0]
        reqMessage = reqMessaging["message"]

        if reqObject == "page":
            if isReviewRequestReply(reqMessaging):
                logging.info("Received review message with rating.")
                # TODO: store review in db
                haoPrint("REVIEW_RECEIVED - ", {
                    "rating": reqMessage["text"],
                    "reviewerId": reqMessaging["sender"]["id"],
                    "reviewedId": reqMessaging["recipient"]["id"]
                })
            elif containsThanks(reqMessage["text"]):
                thankerId = reqMessaging["sender"]["id"]
                logging.info("Sending `you're welcome` message.", thankerId)
                sendMessageToUser(thankerId, YOURE_WELCOME_MESSAGE_TEXT)
                logging.info("Sent `you're welcome` message.", thankerId)

        return HttpResponse("MESSAGE_RECEIVED - " + reqMessage["text"])
