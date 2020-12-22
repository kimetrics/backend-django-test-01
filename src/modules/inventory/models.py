import decimal
from django.db import models
from django.core.exceptions import ValidationError


"""
Modelo que representa un producto (p. ej. Coca-Cola 500ml, 800.00, 500).
"""
class Product(models.Model):
    description = models.TextField(max_length=100)
    unit_price = models.DecimalField(max_digits=7, decimal_places=2)
    stock = models.IntegerField() 