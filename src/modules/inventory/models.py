from django.db import models


class Product(models.Model):

    description = models.TextField(max_length=200)
    unit_price = models.IntegerField() 
    stock = models.IntegerField()