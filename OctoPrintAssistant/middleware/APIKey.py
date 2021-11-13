from django.http import HttpResponse
from OctoPrintAssistant.constants import API_KEY
class APIKeyMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if 'x-api-key' not in request.headers:
            print("No API Key")
            return HttpResponse("API Key required", status=401)

        if request.headers['x-api-key'] != API_KEY:
            print("wrong api key")
        return self.get_response(request)


    def process_exception(self, request, exception): 
        return HttpResponse("in exception")