from rest_framework import serializers

from order.models import Order, OrderItem


class OrderSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(
        many=True, queryset=OrderItem.objects.all()
    )

    class Meta:
        model = Order
        fields = ("id", "date", "status", "user", "products")


class OrderCreateSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(
        many=True, queryset=OrderItem.objects.all()
    )

    class Meta:
        model = Order
        fields = ("id", "date", "user", "products")
