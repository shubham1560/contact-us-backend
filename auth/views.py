from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.schemas import ManualSchema
from rest_framework.compat import coreapi, coreschema
from rest_framework.views import APIView
from rest_framework import parsers, renderers
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.response import Response
from sys_user.models import SysUser


class ObtainAuthTokenViewSet(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer
    if coreapi is not None and coreschema is not None:
        schema = ManualSchema(
            fields=[
                coreapi.Field(
                    name="username",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Username",
                        description="Valid username for authentication",
                    ),
                ),
                coreapi.Field(
                    name="password",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Password",
                        description="Valid password for authentication",
                    ),
                ),
            ],
            encoding="application/json",
        )

    def post(self, request, *args, **kwargs):
        # breakpoint()
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        user = authenticate(request=None,
                            username=request.data['username'], password=request.data['password'])

        if user:
            try:
                token = Token.objects.get(user=user)
                return Response({'token': token.key}, status=status.HTTP_200_OK)
            except ObjectDoesNotExist:
                pass
        else:
            try:
                user = SysUser.objects.get(username=request.data['username'])
                response = {'message': 'Incorrect Password'}
            except ObjectDoesNotExist:
                response = {'message': "The user with this email address doesn't exist"}

            return Response(response, status=status.HTTP_400_BAD_REQUEST)



