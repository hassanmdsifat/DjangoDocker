from django.http import JsonResponse


def Index(request):
    return JsonResponse({
        'status': 'Welcome'
    })
