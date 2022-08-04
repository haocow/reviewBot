import json
import logging

from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from reviewBot.utils.messages import sendMessageToUser

@require_http_methods(["POST"])
def transactions(request):
    # stubbed out endpoint to emulate a transaction being completed
    reqBodyStr = request.body
    reqBodyObj = json.loads(reqBodyStr)
    userId = reqBodyObj["userId"]

    messageText = "Thank you so much for your purchase!  Please leave a review for HaoStore."
    sendMessageToUser(userId, messageText)

    logging.info("TRANSACTION_COMPLETED", userId)
    return HttpResponse("TRANSACTION_COMPLETED")
