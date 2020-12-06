from rest_framework import serializers
from modules.inventory.models import Product

class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = ('description','unit_price','stock') 