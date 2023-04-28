from rest_framework.generics import CreateAPIView

from apps.canban.models import Column
from .serializers import ColumnCreateSerializer


class ColumnCreateAPIView(CreateAPIView):
    queryset = Column.objects.all()
    serializer_class = ColumnCreateSerializer


__all__ = ["ColumnCreateAPIView"]
