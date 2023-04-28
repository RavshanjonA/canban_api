from rest_framework.serializers import ModelSerializer

from apps.cart.models import CartOrderItem


class CartOrderItemListSerializer(ModelSerializer):
    class Meta:
        model = CartOrderItem
        fields = ['product', 'delivery_service', 'quantity', 'price']
