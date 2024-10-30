from django.db import models

from SovaStore import settings
from store.models import Product


class Order(models.Model):
    class StatusChoices(models.TextChoices):
        PROCESSING = "Processing"
        IN_PROCESS = "In process"
        DONE = "Done"

    date = models.DateField(auto_now_add=True)
    status = models.CharField(
        max_length=100,
        choices=StatusChoices.choices,
        default=StatusChoices.PROCESSING,
        editable=False,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="orders"
    )

    def __str__(self):
        return f"{self.user} - {self.date}"

    class Meta:
        ordering = ("-date",)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="items")
    quantity = models.PositiveIntegerField(default=1)
