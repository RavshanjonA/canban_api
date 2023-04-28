from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from .permissions import IsTheOwner
from .serializers import BoardRetrieveSerializer
from ....models import Board


class BoardRetrieveAPIView(RetrieveAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardRetrieveSerializer
    permission_classes = [IsAuthenticated, IsTheOwner]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


__all__ = ["BoardRetrieveAPIView"]
