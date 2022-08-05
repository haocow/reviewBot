import logging
import os
import requests

from reviewBot.utils.constants import YOURE_WELCOME_MESSAGE_TEXT
from reviewBot.utils.print import haoPrint
from reviewBot.utils.facebook import (GRAPH_BASE_URL, getPageAccessTokenQueryParams)

MESSAGES_URL = GRAPH_BASE_URL+"/v2.6/me/messages"
PAGE_ACCESS_TOKEN_URL = GRAPH_BASE_URL + "/"+ os.environ.get('PAGE_ID') + getPageAccessTokenQueryParams(os.environ.get('USER_ACCESS_TOKEN'))

def sendMessageToUser(recipientId, message):
    # get page access token
    respPageAccessToken = requests.get(PAGE_ACCESS_TOKEN_URL)
    respBody = respPageAccessToken.json()
    pageAccessToken = respBody["access_token"]

    # send message
    reqParams= {
        "access_token": pageAccessToken,
    }
    reqBody = {
        "recipient": {
            "id": recipientId,
        },
        "message": {
            "text": message,
        },
    }
    result = requests.post(MESSAGES_URL, json=reqBody, params=reqParams)
    if result.status_code != 200:
        logging.error("Failed to send message to user.", recipientId)

    return

def containsThanks(text: str):
    return "thank" in text.lower()

def isReviewRequestReply(messaging):
    message = messaging["message"]
    if "reply_to" not in message:
        return False
    return isReviewRequest(message["reply_to"]["mid"])
    
def isReviewRequest(messageId):
    # TODO: confirm that this is a valid review request
    # for now, just always return True if there's a reply_to id
    return True
