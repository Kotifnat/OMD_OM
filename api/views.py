from rest_framework.generics import ListCreateAPIView
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
