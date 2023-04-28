from rest_framework.generics import CreateAPIView

from apps.canban.models import Board
from .serializers import BoardCreateSerializer


class BoardCreateAPIView(CreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardCreateSerializer


__all__ = ["BoardCreateAPIView"]
