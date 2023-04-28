from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.canban.models import Column
from .permissions import IsTheOwner
from .serializers import ColumnUpdateSerializer


class ColumnUpdateAPIView(UpdateAPIView):
    queryset = Column.objects.all()
    serializer_class = ColumnUpdateSerializer
    permission_classes = [IsAuthenticated, IsTheOwner]

    def get_queryset(self):
        return self.queryset.filter(board__user=self.request.user)


__all__ = ["ColumnUpdateAPIView"]
