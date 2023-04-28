from rest_framework.generics import CreateAPIView

from apps.canban.models import Task
from .serializers import TaskCreateSerializer


class TaskCreateAPIView(CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCreateSerializer


__all__ = ["TaskCreateAPIView"]
