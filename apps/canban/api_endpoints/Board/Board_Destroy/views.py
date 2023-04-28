from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from apps.canban.models import Board
from .permissions import IsTheOwner


class BoardDestroyAPIView(DestroyAPIView):
    queryset = Board.objects.all()
    permission_classes = [IsAuthenticated, IsTheOwner]


__all__ = ["BoardDestroyAPIView"]
