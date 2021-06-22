from django.urls import path, include
from .views import MyTokenObtainView

urlpatterns = [
    path('user/token/', MyTokenObtainView.as_view(), name='token_obtain'),
]
