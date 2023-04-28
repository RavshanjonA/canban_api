from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from .permissions import IsTheOwner
from .serializers import TaskListSerializer
from ....models import Task


class TaskListAPIView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskListSerializer
    permission_classes = [IsAuthenticated, IsTheOwner]
    lookup_field = 'column_id'

    def get_queryset(self):
        return self.queryset.filter(column__board__user=self.request.user)


__all__ = ["TaskListAPIView"]
