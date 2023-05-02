# from allauth.account.adapter import get_adapter
# from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
# from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
# from allauth.socialaccount.providers.oauth2.client import OAuth2Client
# from dj_rest_auth.views import LoginView as RestLoginView
# from django.conf import settings
#
# from . import serializers
#
#
# class SocialLoginView(RestLoginView):
#     serializer_class = serializers.SocialAuthLoginSerializer
#
#     def process_login(self):
#         get_adapter(self.request).login(self.request, self.user)
#
#
# class GoogleLogin(SocialLoginView):
#     adapter_class = GoogleOAuth2Adapter
#     callback_url = settings.OAUTH_CALLBACK_URL
#     # callback_url = "http://127.0.0.1:8000/callback"
#     client_class = OAuth2Client
#
#
# class FacebookLogin(SocialLoginView):
#     adapter_class = FacebookOAuth2Adapter
#
#
# __all__ = ["GoogleLogin", "FacebookLogin"]

from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView


# class GoogleLogin(SocialLoginView):  # if you want to use Authorization Code Grant, use this
#     adapter_class = GoogleOAuth2Adapter
#     callback_url = "http://127.0.0.1:8000/callback"
#     client_class = OAuth2Client


class GoogleLogin(SocialLoginView):  # if you want to use Implicit Grant, use this
    adapter_class = GoogleOAuth2Adapter


__all__ = ["GoogleLogin"]
