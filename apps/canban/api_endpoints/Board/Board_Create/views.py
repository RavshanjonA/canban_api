from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from apps.canban.models import Board
from .serializers import BoardCreateSerializer


class BoardCreateAPIView(CreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cd = serializer.validated_data
        new_board = Board.objects.create(user=self.request.user, title=cd['title'])
        new_board.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


__all__ = ["BoardCreateAPIView"]
