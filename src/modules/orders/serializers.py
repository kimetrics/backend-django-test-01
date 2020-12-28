from rest_framework import serializers

from .models import Order, OrderItem


def get_items_for_serialized_order(data):
    items = data.pop('items')
    products = []
    for item in items:
        data = {
            'product_id': item['product']['id'],
            'quantity': item['quantity']
        }
        products.append(data)
    return products


class OrderItemListSerializer(serializers.ModelSerializer):
    description = serializers.StringRelatedField(source='product.description')
    unit_price = serializers.IntegerField(source='product.unit_price')

    class Meta:
        model = OrderItem
        fields = ['description', 'quantity', 'unit_price', 'total']


class OrderItemCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='product.id')

    class Meta:
        model = OrderItem
        fields = ['quantity', 'id']


class OrderListSerializer(serializers.ModelSerializer):
    items = OrderItemListSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'items', 'total']


class OrderCreateSerializer(serializers.ModelSerializer):
    items = OrderItemCreateSerializer(many=True)

    class Meta:
        model = Order
        fields = ['items']

    def create(self, validated_data):
        items = get_items_for_serialized_order(validated_data)
        order = Order.create_order(items)
        return order
