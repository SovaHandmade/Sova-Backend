import os
import uuid
from PIL import Image
from django.db import models
from django.utils.text import slugify


class Tag(models.Model):
    name = models.CharField(max_length=25, unique=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Topic(Tag):
    pass


class Form(Tag):
    pass


def product_image_file_path(instance, filename):
    _, extension = os.path.splitext(filename)
    filename = f"{slugify(instance.name)}-{uuid.uuid4()}{extension}"

    return os.path.join("uploads/products/", filename)


class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(null=True, upload_to=product_image_file_path)
    size = models.CharField(max_length=100)
    material = models.CharField(max_length=100)
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
    price = models.PositiveIntegerField(default=0)
    in_stock = models.BooleanField(blank=False, null=False, default=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        width, height = img.size

        new_side = min(width, height)

        left = (width - new_side) // 2
        top = (height - new_side) // 2
        right = (width + new_side) // 2
        bottom = (height + new_side) // 2

        img = img.crop((left, top, right, bottom))
        img.save(self.image.path, optimize=True, quality=85)

    def __str__(self):
        return self.name + " - " + self.size
