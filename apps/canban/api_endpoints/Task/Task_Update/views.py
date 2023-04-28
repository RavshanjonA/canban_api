from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.canban.models import Task
from .permissions import IsTheOwner
from .serializers import TaskUpdateSerializer


class TaskUpdateAPIView(UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskUpdateSerializer
    permission_classes = [IsAuthenticated, IsTheOwner]

    def get_queryset(self):
        return self.queryset.filter(column__board__user=self.request.user)


__all__ = ["TaskUpdateAPIView"]
