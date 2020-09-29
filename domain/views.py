from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from .models import Domain


class GetDomainDetailViewSet(APIView):
    permission_classes = (IsAuthenticated, )

    class GetDomainDetailSerializer(serializers.ModelSerializer):
        class Meta:
            model = Domain
            fields = ('active', 'description', 'name', 'sys_created_on', 'api_key')

    def get(self, request, format=None):
        domain = Domain.objects.get(domain_path=request.user.domain_path)
        result = self.GetDomainDetailSerializer(domain, many=False)
        return Response(result.data, status=status.HTTP_200_OK)