from django.contrib.auth import authenticate, login, logout
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.parsers import FormParser
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import LoginSerializer


class LoginAPIView(APIView):
    permission_classes = [AllowAny]
    parser_classes = [FormParser]

    @swagger_auto_schema(request_body=LoginSerializer)
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            vd = serializer.validated_data
            user = authenticate(request, username=vd['login'], password=vd['password'])
            if user:
                if user.is_active:
                    login(request, user)
                    return Response(status=status.HTTP_200_OK)
                else:
                    return Response({'status': 'User not active'})
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        logout(request)
        return Response(status=status.HTTP_200_OK)


__all__ = ['LoginAPIView', 'LogoutAPIView']
