from rest_framework_simplejwt.views import TokenObtainPairView
from api.serializers import MyTokenObtainSerializer


class MyTokenObtainView(TokenObtainPairView):
    serializer_class = MyTokenObtainSerializer
