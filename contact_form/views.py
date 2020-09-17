from django_countries import Countries
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import serializers, status
from .models import ContactForm
from rest_framework.response import Response
from .services import insert_contact_data, get_related_forms_records


# Create your views here.

class SerializableCountryField(serializers.ChoiceField):
    def __init__(self, **kwargs):
        super(SerializableCountryField, self).__init__(choices=Countries())

    def to_representation(self, value):
        if value in ('', None):
            return '' # normally here it would return value. which is Country(u'') and not serialiable
        return super(SerializableCountryField, self).to_representation(value)


class ContactUsFormView(APIView):
    permission_classes = (IsAuthenticated, )
    country = SerializableCountryField(allow_blank=True)

    class ContactUsFormSerializer(serializers.ModelSerializer):
        class Meta:
            model = ContactForm
            fields = ('id', 'first_name', 'last_name',
                      'country', 'name', 'email', 'subject', 'message', 'anything_else')

    def get(self, request, format=None):
        # breakpoint()
        contacts_data = get_related_forms_records(request)
        result = self.ContactUsFormSerializer(contacts_data, many=True)
        return Response(result.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        insert_contact_data(request)
        return Response('Inserted data', status=status.HTTP_201_CREATED)
        # pass

