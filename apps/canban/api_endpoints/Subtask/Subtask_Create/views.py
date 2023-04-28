from rest_framework.generics import CreateAPIView

from apps.canban.models import Subtask
from .serializers import SubtaskCreateSerializer


class SubtaskCreateAPIView(CreateAPIView):
    queryset = Subtask.objects.all()
    serializer_class = SubtaskCreateSerializer


__all__ = ["SubtaskCreateAPIView"]
