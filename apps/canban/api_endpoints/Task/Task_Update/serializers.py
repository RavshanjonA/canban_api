from rest_framework import serializers

from apps.cart.models import CartOrderItem


class CartOrderItemUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartOrderItem
        fields = ["delivery_service", "quantity"]
