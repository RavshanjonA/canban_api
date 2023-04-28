from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from ....models import CartOrderItem
from .permissions import IsTheOwner
from .serializers import CartOrderItemListSerializer


class CartOrderItemListAPIView(ListAPIView):
    queryset = CartOrderItem.objects.all()
    serializer_class = CartOrderItemListSerializer
    permission_classes = [IsAuthenticated, IsTheOwner]

    def get_queryset(self):
        user = self.request.user
        self.queryset = self.queryset.filter(cart=user.cart)


__all__ = ["CartOrderItemListAPIView"]
