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
            "topic",
            "form",
            "price_display",
        )


class ProductListSerializer(ProductSerializer):
    class Meta:
        model = Product
        fields = ("name", "image", "size", "price_display")


class ProductDetailSerializer(ProductSerializer):
    topic_name = serializers.CharField(source="topic.name", read_only=True)
    form_name = serializers.CharField(source="form.name", read_only=True)

    class Meta:
        model = Product
        fields = (
            "name",
            "image",
            "size",
            "color",
            "material",
            "description",
            "topic_name",
            "form_name",
            "price_display",
        )


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "image")
