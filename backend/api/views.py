import json
from django.http import JsonResponse

def api_home(request, *args, **kwargs):

    body = request.body
    data = {}
    try:
        data = json.loads(body)
    except Exception as e:
        pass
    print(data) 
    return JsonResponse(data)