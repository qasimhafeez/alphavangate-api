from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .utils import get_rate


class GetRate(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    def get(self, request):
        a = Response({'Exchange_rate': get_rate()})
        return a

    def post(self, request):
        pass
