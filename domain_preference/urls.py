from django.urls import path
from .views import ChangeUserDomainPreference, ChangeUserDomainPeferenceField

urlpatterns = [
    path('v1/domain_preference/', ChangeUserDomainPreference.as_view()),
    path('v1/domain_preference/change/', ChangeUserDomainPeferenceField.as_view()),
    # path('v1/contact-us/post/', )
]