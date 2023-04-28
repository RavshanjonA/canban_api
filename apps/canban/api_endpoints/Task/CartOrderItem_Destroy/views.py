from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from apps.cart.models import CartOrderItem
from .permissions import IsTheOwner


class CartOrderItemDestroyAPIView(DestroyAPIView):
    queryset = CartOrderItem.objects.all()
    permission_classes = [IsAuthenticated, IsTheOwner]


__all__ = ["CartOrderItemDestroyAPIView"]
