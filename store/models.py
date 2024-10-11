from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Form(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    image = ...
    size = models.CharField(max_length=255)
    material = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    description = models.TextField(blank=False, null=False)
    tags = models.ManyToManyField(Topic, Form, blank=False, null=False)
    price = models.IntegerField()
    in_stock = models.BooleanField(blank=False, null=False, default=False)
