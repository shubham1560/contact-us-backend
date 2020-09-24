from django.urls import path, include
from .views import ObtainAuthTokenViewSet

urlpatterns = [
    path('token/get_token/', ObtainAuthTokenViewSet.as_view())
]

