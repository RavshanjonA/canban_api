from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from apps.canban.models import Column
from .permissions import IsTheOwner


class ColumnDestroyAPIView(DestroyAPIView):
    queryset = Column.objects.all()
    permission_classes = [IsAuthenticated, IsTheOwner]

    def get_queryset(self):
        return self.queryset.filter(board__user=self.request.user)


__all__ = ["ColumnDestroyAPIView"]
