from django.db import models
from django.core.exceptions import ValidationError


"""
Modelo que representa una orden.
"""
class Order(models.Model):
    items = models.CharField(max_length=200, default='[]')
    total = models.IntegerField() 