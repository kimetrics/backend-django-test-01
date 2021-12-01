from django.db import models
from django.db.models.base import Model


class Product(models.Model):
    description=models.CharField(max_length=250)
    unit_price=models.FloatField()
    stock=models.IntegerField()
