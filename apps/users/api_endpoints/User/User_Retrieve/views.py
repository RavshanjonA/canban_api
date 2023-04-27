from rest_framework.generics import RetrieveAPIView

from .serializers import UserRetrieveSerializer
from ....models import User


class UserRetrieveAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserRetrieveSerializer


__all__ = ['UserRetrieveAPIView']
