from rest_framework.generics import UpdateAPIView
from rest_framework.parsers import MultiPartParser, FormParser

from apps.users.permissions import IsTheSameUser
from .serializers import UserUpdateSerializer
from ....models import User


class UserUpdateAPIView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    permission_classes = [IsTheSameUser]
    parser_classes = [MultiPartParser, FormParser]


__all__ = ['UserUpdateAPIView']
