from django.db import models
from .managers import UserManager
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(
        "Email Address",
        unique=True,
    )

    USERNAME_FIELD = "full_name"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.full_name
