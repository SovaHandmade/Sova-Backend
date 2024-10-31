from rest_framework import serializers

from order.models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    total_price = serializers.ReadOnlyField()

    class Meta:
        model = OrderItem
        fields = ("id", "product_id", "quantity", "total_price")


class OrderSerializer(serializers.ModelSerializer):
    total_price = serializers.ReadOnlyField()
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ("id", "date", "status", "user", "items", "total_price")


class OrderCreateSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(
        many=True, queryset=OrderItem.objects.all()
    )

    class Meta:
        model = Order
        fields = ("id", "date", "user", "products")
