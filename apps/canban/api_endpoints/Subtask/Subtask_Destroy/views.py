from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from apps.canban.models import Subtask
from .permissions import IsTheOwner


class SubtaskDestroyAPIView(DestroyAPIView):
    queryset = Subtask.objects.all()
    permission_classes = [IsAuthenticated, IsTheOwner]

    def get_queryset(self):
        return self.queryset.filter(task__column__board__user=self.request.user)


__all__ = ["SubtaskDestroyAPIView"]
