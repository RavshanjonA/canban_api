from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import BoardListSerializer
from ....models import Board


class BoardListAPIView(ListAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


__all__ = ["BoardListAPIView"]
