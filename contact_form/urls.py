from django.urls import path
from .views import ContactUsListView, ContactUsPostView

urlpatterns = [
    path('v1/contact-us/get/', ContactUsListView.as_view()),
    path('v1/contact-us/post/', ContactUsPostView.as_view())
]