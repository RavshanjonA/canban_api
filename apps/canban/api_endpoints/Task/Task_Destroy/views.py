from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from apps.canban.models import Task
from .permissions import IsTheOwner


class TaskDestroyAPIView(DestroyAPIView):
    queryset = Task.objects.all()
    permission_classes = [IsAuthenticated, IsTheOwner]

    def get_queryset(self):
        return self.queryset.filter(column__board__user=self.request.user)


__all__ = ["TaskDestroyAPIView"]
