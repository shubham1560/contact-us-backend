from django.urls import path
from .views import GetDomainDetailViewSet

urlpatterns = [
    path('v1/domain/details/', GetDomainDetailViewSet.as_view()),
]