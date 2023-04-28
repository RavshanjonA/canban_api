from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.canban.models import Board
from .permissions import IsTheOwner
from .serializers import BoardUpdateSerializer


class BoardUpdateAPIView(UpdateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardUpdateSerializer
    permission_classes = [IsAuthenticated, IsTheOwner]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


__all__ = ["BoardUpdateAPIView"]
