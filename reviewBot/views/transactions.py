import json
import logging

from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from reviewBot.utils.constants import REVIEW_REQUEST_MESSAGE_TEXT
from reviewBot.utils.messages import sendMessageToUser

@require_http_methods(["POST"])
def transactions(request):
    # stubbed out endpoint to emulate a transaction being completed
    reqBodyStr = request.body
    reqBodyObj = json.loads(reqBodyStr)
    userId = reqBodyObj["userId"]

    sendMessageToUser(userId, REVIEW_REQUEST_MESSAGE_TEXT)

    logging.info("TRANSACTION_COMPLETED", userId)
    return HttpResponse("TRANSACTION_COMPLETED")
