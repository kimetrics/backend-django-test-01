from django.db import models


class Order(models.Model):
    
    items = models.CharField(max_length=200, default='[]')
    total = models.IntegerField()

    @property
    def item(self):
        return json.loads(self.items)

    @item.setter
    def item(self, value):
        self.items = json.dumps(self.item + value)