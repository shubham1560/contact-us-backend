from django.urls import path
from .views import ContactUsListView, ContactUsPostView, ContactUsChangeView

urlpatterns = [
    path('v1/contact-us/get/<int:start>/', ContactUsListView.as_view()),
    path('v1/contact-us/post/', ContactUsPostView.as_view()),
    path('v1/contact-us/change/', ContactUsChangeView.as_view())
]