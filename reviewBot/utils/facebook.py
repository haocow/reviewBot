GRAPH_BASE_URL = "https://graph.facebook.com"

def getPageAccessTokenQueryParams(userAccessToken):
    return "?fields=access_token&access_token=" + userAccessToken
