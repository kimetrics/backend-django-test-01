from django.db import models


class Product(models.Model):
    description = models.TextField(
        'description',
        max_length=255,
        null=False,
        blank=False,
        default=None
    )

    unit_price = models.IntegerField(
        'unit price',
        default=0,
        null=False
    )

    stock = models.IntegerField(
        'stock',
        default=0,
        null=False
    )
