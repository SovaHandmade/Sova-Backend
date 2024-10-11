from rest_framework import serializers

from store.models import Topic, Form, Product


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ("id", "name")


class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = ("id", "name")


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "image",
            "size",
            "material",
            "color",
            "description",
            "tags",
            "price",
        )


class ProductListSerializer(ProductSerializer):
    class Meta:
        model = Product
        fields = ("name", "image", "size", "price")


class ProductDetailSerializer(ProductSerializer):
    topic = TopicSerializer(many=False, read_only=True)
    form = FormSerializer(many=False, read_only=True)

    class Meta:
        model = Product
        fields = ("name", "image", "size", "price", "topic", "form")


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "image")
