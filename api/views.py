import json

from django.http import HttpResponse
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from api.serializers import MyTokenObtainSerializer
from .serializers import CBUModelSerializer
from .models import CBU


class MyTokenObtainView(TokenObtainPairView):
    serializer_class = MyTokenObtainSerializer


class CBUListCreateView(ListCreateAPIView):
    serializer_class = CBUModelSerializer

    def get_queryset(self):
        owner = self.request.user
        return CBU.objects.filter(user=owner)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(json.dumps(serializer.data, ensure_ascii=False), content_type="application/json")
