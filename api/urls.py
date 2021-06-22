from django.urls import path, include
from .views import MyTokenObtainView, CBUListCreateView

urlpatterns = [
    path('user/token/', MyTokenObtainView.as_view(), name='token_obtain'),
    path('curve/', CBUListCreateView.as_view(), name='cbu_list_create'),
]
