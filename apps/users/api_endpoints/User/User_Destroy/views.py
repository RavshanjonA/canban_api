from rest_framework.generics import DestroyAPIView

from apps.users.permissions import IsTheSameUser
from apps.users.models import User


class UserDestroyAPIView(DestroyAPIView):
    permission_classes = [IsTheSameUser]
    queryset = User.objects.all()


__all__ = ['UserDestroyAPIView']
