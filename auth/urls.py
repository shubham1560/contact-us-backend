from django.urls import path, include
from .views import ObtainAuthTokenViewSet, CreateUserSystemViewSet

urlpatterns = [
    path('token/get_token/', ObtainAuthTokenViewSet.as_view()),
    path('user/register/system/', CreateUserSystemViewSet.as_view()),
    # path('user/register/google/'),
    # path('user/register/facebook/'),
    # path('user/activate/'),
    # path('user/password_reset/'),
    # path('user/send_reset_link/'),
    # path('token/valid/'),
    # path('token/user/'),
]

