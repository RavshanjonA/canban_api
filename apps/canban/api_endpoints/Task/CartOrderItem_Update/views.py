from rest_framework.generics import UpdateAPIView
from rest_framework.parsers import FormParser
from rest_framework.permissions import IsAuthenticated

from apps.cart.models import CartOrderItem
from .permissions import IsTheOwner
from .serializers import CartOrderItemUpdateSerializer


class CartOrderItemUpdateAPIView(UpdateAPIView):
    queryset = CartOrderItem.objects.all()
    serializer_class = CartOrderItemUpdateSerializer
    permission_classes = [IsAuthenticated, IsTheOwner]
    parser_classes = [FormParser]


__all__ = ["CartOrderItemUpdateAPIView"]
