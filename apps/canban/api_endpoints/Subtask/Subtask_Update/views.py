from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.canban.models import Subtask
from .permissions import IsTheOwner
from .serializers import SubtaskUpdateSerializer


class SubtaskUpdateAPIView(UpdateAPIView):
    queryset = Subtask.objects.all()
    serializer_class = SubtaskUpdateSerializer
    permission_classes = [IsAuthenticated, IsTheOwner]


__all__ = ["SubtaskUpdateAPIView"]
