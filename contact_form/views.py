from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import serializers, status
from .models import ContactForm
from rest_framework.response import Response


# Create your views here.

class ContactUsFormView(APIView):
    permission_classes = (IsAuthenticated, )

    class ContactUsFormSerializer(serializers.ModelSerializer):
        class Meta:
            model = ContactForm
            fields = ('id', 'first_name', 'last_name',
                      'country', 'name', 'email', 'subject', 'message', 'anything_else')

    def get(self, request, format=None):
        # breakpoint()
        contacts_data = ContactForm.objects.all()
        result = self.ContactUsFormSerializer(contacts_data, many=True)
        return Response(result.data, status=status.HTTP_200_OK)

