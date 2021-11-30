import requests
from django.http import HttpResponse
from OctoPrintAssistant.constants import API_KEY
from OctoPrintAssistant.utils import get_connection_status


class VerifyConnectionMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            res = get_connection_status()
        except requests.ConnectionError as e:
            print("Connection Error")
            return HttpResponse("Connection Error: fail to connect. OctoPrint server may be offline.", status=500)
        if res.status_code == 403:
            return HttpResponse("Forbidden, probably invalid API Key", status=403)
        elif res.status_code != 200:
            return HttpResponse("Unknown Error from Connection Verification.", status=400)
        return self.get_response(request)

    def process_exception(self, request, exception):
        return HttpResponse("Connection Exception. OctoPrint Server may be offline.")
