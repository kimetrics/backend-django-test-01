from django.db import models
from django.core.exceptions import ValidationError


"""
Modelo que representa una orden.
"""
class Order(models.Model):
    items = models.CharField(max_length=400, default='[]')
    total = models.DecimalField(max_digits=7, decimal_places=2)