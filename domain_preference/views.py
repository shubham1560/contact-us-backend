from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import serializers, status
from domain_preference.models import DomainPreference
from rest_framework.response import Response
from .services import change_domain_preference


class ChangeUserDomainPreference(APIView):
    permission_classes = (IsAuthenticated, )

    class DomainPreferences(serializers.ModelSerializer):
        class Meta:
            model = DomainPreference
            fields = ('id', 'first_name', 'last_name',
                      'name', 'email', 'subject', 'message', 'anything_else',
                      'phone_number')

    def post(self, request, format=None):
        change_domain_preference(request)
        return Response('', status=status.HTTP_201_CREATED)
