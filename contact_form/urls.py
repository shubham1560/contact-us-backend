from django.urls import path
from .views import ContactUsFormView

urlpatterns = [
    path('v1/contact-us/', ContactUsFormView.as_view())
]