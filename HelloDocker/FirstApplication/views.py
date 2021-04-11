import json

import requests
from django.http import JsonResponse
from HelloDocker.settings import API_ROOT


def Index(request):
    all_products_call = requests.get(API_ROOT + '/api/product/all/')
    all_products = json.loads(all_products_call.content)
    return JsonResponse({
        'data': all_products.get('data', {}),
    })
