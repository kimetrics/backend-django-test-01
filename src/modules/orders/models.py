from django.db import models


class Order(models.Model):
    items = models.JSONField()
    total = models.FloatField()
