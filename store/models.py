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
    filename = f"{slugify(instance.title)}-{uuid.uuid4()}{extension}"

    return os.path.join("uploads/movies/", filename)


class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(null=True, upload_to=product_image_file_path)
    size = models.CharField(max_length=255)
    material = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    description = models.TextField(blank=False, null=False)
    topic = models.ManyToManyField(Topic, blank=False, null=False)
    form = models.ManyToManyField(Form, blank=False, null=False)
    price = models.IntegerField()
    in_stock = models.BooleanField(blank=False, null=False, default=False)
