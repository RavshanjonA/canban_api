from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from .permissions import IsTheOwner
from .serializers import SubtaskListSerializer
from ....models import Subtask


class SubtaskListAPIView(ListAPIView):
    queryset = Subtask.objects.all()
    serializer_class = SubtaskListSerializer
    permission_classes = [IsAuthenticated, IsTheOwner]
    lookup_field = 'task_id'


__all__ = ["SubtaskListAPIView"]
