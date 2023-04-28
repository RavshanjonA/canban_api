from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from .permissions import IsTheOwner
from .serializers import SubtaskListSerializer
from ....models import Subtask


class SubtaskListAPIView(ListAPIView):
    queryset = Subtask.objects.all()
    serializer_class = SubtaskListSerializer
    permission_classes = [IsAuthenticated, IsTheOwner]

    def get_queryset(self):
        return self.queryset.filter(task__column__board__user=self.request.user)
    # todo add filter by task


__all__ = ["SubtaskListAPIView"]
