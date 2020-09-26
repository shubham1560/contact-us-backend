from django_countries import Countries
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import serializers, status
from .models import ContactForm
from rest_framework.response import Response
from .services import insert_contact_data, get_related_forms_records, get_preference_array
from domain_preference.models import DomainPreference


# Create your views here.

class SerializableCountryField(serializers.ChoiceField):
    def __init__(self, **kwargs):
        super(SerializableCountryField, self).__init__(choices=Countries())

    def to_representation(self, value):
        if value in ('', None):
            return '' # normally here it would return value. which is Country(u'') and not serialiable
        return super(SerializableCountryField, self).to_representation(value)


class ContactUsListView(APIView):
    permission_classes = (IsAuthenticated, )
    country = SerializableCountryField(allow_blank=True)

    class ContactUsFormSerializer(serializers.ModelSerializer):
        class Meta:
            model = ContactForm
            fields = ('id', 'first_name', 'last_name',
                      'name', 'email', 'subject', 'message', 'anything_else',
                      'phone_number', 'sys_created_on')

    class DomainPreferenceSerializer(serializers.ModelSerializer):
        class Meta:
            model = DomainPreference
            fields = ('id', 'first_name', 'last_name', 'name', 'email', 'subject',
                      'message', 'anything_else', 'phone_number')

    def get(self, request, start, end, format=None):
        contacts_data = get_related_forms_records(request, start, end)
        domain_preference = get_preference_array(request)
        result = self.ContactUsFormSerializer(contacts_data, many=True)
        preference = self.DomainPreferenceSerializer(domain_preference, many=True)
        response = {
            "list": result.data,
            "preference": preference.data,
        }
        return Response(response, status=status.HTTP_200_OK)

    # def post(self, request, format=None):
    #     insert_contact_data(request)
    #     return Response('Inserted data', status=status.HTTP_201_CREATED)
    #     # pass


class ContactUsPostView(APIView):
    # permission_classes = (IsAuthenticated, )
    country = SerializableCountryField(allow_blank=True)

    class ContactUsFormSerializer(serializers.ModelSerializer):
        class Meta:
            model = ContactForm
            fields = ('id', 'first_name', 'last_name',
                      'country', 'name', 'email', 'subject', 'message', 'anything_else',
                      'domain', 'domain_path')

    def post(self, request, format=None):
        insert_contact_data(request)
        return Response('Inserted data', status=status.HTTP_201_CREATED)

