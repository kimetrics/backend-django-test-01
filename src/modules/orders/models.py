from django.db import models

from modules.inventory.models import Product


class Order(models.Model):

    @property
    def total(self):
        return sum([item.total for item in self.items.all()])

    @classmethod
    def create_order(cls, items):
        order = cls.objects.create()

        orderitem_data = {
            'order': order
        }

        for item in items:
            item['product'] = Product.objects.get(pk=item['product_id'])
            orderitem_data.update(**item)
            order_item = OrderItem.objects.create(**orderitem_data)
            order_item.product.stock -= order_item.quantity
            order_item.product.save()

        order.save()
        return order


class OrderItem(models.Model):
    order = models.ForeignKey(
        'orders.Order',
        related_name='items',
        default=None,
        on_delete=models.CASCADE
    )

    product = models.ForeignKey(
        'inventory.Product',
        verbose_name='product',
        default=None,
        on_delete=models.CASCADE
    )

    quantity = models.IntegerField(
        'quuantity',
        null=False,
        blank=False,
        default=0
    )

    @property
    def total(self):
        return self.product.unit_price * self.quantity
