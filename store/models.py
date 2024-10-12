import os
import uuid

from django.db import models
from django.utils.text import slugify


class Topic(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Form(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


def product_image_file_path(instance, filename):
    _, extension = os.path.splitext(filename)
    filename = f"{slugify(instance.name)}-{uuid.uuid4()}{extension}"

    return os.path.join("uploads/products/", filename)


class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(null=True, upload_to=product_image_file_path)
    size = models.CharField(max_length=255)
    material = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    description = models.TextField(blank=False, null=False)
    topic = models.ForeignKey(
        to=Topic,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="products",
    )
    form = models.ForeignKey(
        to=Form,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="products",
    )
    price = models.IntegerField()
    in_stock = models.BooleanField(blank=False, null=False, default=False)
