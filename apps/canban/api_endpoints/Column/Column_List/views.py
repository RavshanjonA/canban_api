from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from .permissions import IsTheOwner
from .serializers import ColumnListSerializer
from ....models import Column


class ColumnListAPIView(ListAPIView):
    queryset = Column.objects.all()
    serializer_class = ColumnListSerializer
    permission_classes = [IsAuthenticated, IsTheOwner]
    lookup_field = 'board_id'

    def get_queryset(self):
        return self.queryset.filter(board__user=self.request.user)


__all__ = ["ColumnListAPIView"]
