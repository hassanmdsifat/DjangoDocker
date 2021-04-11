from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView


class GetAllProducts(APIView):
    def get(self, request):
        data = {
            'product_one': {
                'id': 1,
                'price': 10,
                'quantity': 100
            }
        }
        return Response({
            'data': data
        }, status=HTTP_200_OK)