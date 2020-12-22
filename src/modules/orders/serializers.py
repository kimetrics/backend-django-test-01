from .models import Order
from rest_framework import serializers

class SerializedOrder(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'
    