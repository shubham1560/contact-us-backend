from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import serializers, status
from domain_preference.models import DomainPreference
from rest_framework.response import Response
from .services import change_domain_preference, change_domain_preference_field, get_message_detail_preference


class ChangeUserDomainPreference(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request, device_type, format=None):
        change_domain_preference(request, device_type)
        return Response('', status=status.HTTP_201_CREATED)


class ChangeUserDomainPeferenceField(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request, format=None):
        change_domain_preference_field(request)
        return Response('', status=status.HTTP_201_CREATED)


class GetMessageDetailPreference(APIView):
    permission_classes = (IsAuthenticated, )

    class DomainPreferenceSerailizer(serializers.ModelSerializer):
        class Meta:
            model = DomainPreference
            fields = ['id',
                      "first_name",
                      "last_name", "name",
                      "phone_number", "email", "subject", 'message', "anything_else"]

    def get(self, request, format=None):
        result, exist = get_message_detail_preference(request)
        # breakpoint()
        if exist:
            response = self.DomainPreferenceSerailizer(result, many=False)
            return Response(response.data, status=status.HTTP_200_OK)
        else:
            return Response(result, status=status.HTTP_200_OK)