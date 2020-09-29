from django.urls import path
from .views import ChangeUserDomainPreference, ChangeUserDomainPeferenceField, GetMessageDetailPreference

urlpatterns = [
    path('v1/domain_preference/<str:device_type>/', ChangeUserDomainPreference.as_view()),
    path('v1/domain_preference/change/window/', ChangeUserDomainPeferenceField.as_view()),
    path('v1/domain_preference/get/detail/', GetMessageDetailPreference.as_view()),
    # path('v1/contact-us/post/', )
]