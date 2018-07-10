from django.conf import settings
from django.contrib.auth import get_user_model

from google.auth.transport import requests
from google.oauth2 import id_token
from oauth2_provider.models import get_access_token_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

User = get_user_model()
AccessToken = get_access_token_model()


class AndroidAuthenticationView(APIView):
    CLIENT_ID = settings.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY

    def get(self, request, *args, **kwargs):
        try:
            ID_token = self.request.query_params.get('id_token')
            id_token_info = id_token.verify_oauth2_token(ID_token, requests.Request(), self.CLIENT_ID)

            if id_token_info['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
                raise ValueError('Wrong issuer.')

            user_email = id_token_info['email']
            user = User.objects.get(email=user_email)
            if user:
                token = AccessToken.objects.filter(user=user).last()
                return Response(data={'access_token': token.token})

        except ValueError:
            return Response(data={'error': 'Token is invalid'}, status=status.HTTP_400_BAD_REQUEST)
