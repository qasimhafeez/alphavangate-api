from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .utils import get_rate, get_rate_from_db


class GetRate(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    def get(self, request):
        return Response({'Exchange_rate': get_rate_from_db()})

    def post(self, request):
        return Response({'Exchange_rate': get_rate()})
