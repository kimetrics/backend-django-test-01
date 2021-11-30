from django.shortcuts import render
from rest_framework import serializers, viewsets, status
from .models import Order
from modules.inventory.models import Product
from .serializers import OrderSerializers
from rest_framework.response import Response

# Create your views here.
class OrderViewsets(viewsets.ModelViewSet):
    http_method_names = ['get', 'post']
    queryset=Order.objects.all()
    serializer_class = OrderSerializers

    def create(self, request, *args, **kwargs):
        items = request.data["items"]
        items_order = []
        for i in items:
            p = Product.objects.get(id=i["id"])
            new_stock = p.stock - i["quantity"]
            json_object_p = {
                "description": p.description,
                "quantity": i["quantity"],
                "unit_price": p.unit_price,
                "total": p.unit_price*i["quantity"]
            }
            items_order.append(json_object_p)
            Product.objects.filter(id=i["id"]).update(stock=new_stock)
        
        grand_total = 0
        for i in items_order:
            grand_total+=i["total"]
        order = Order(items=items_order,total=grand_total)
        order.save()
        serializer = OrderSerializers(order)
        return Response(serializer.data,status=status.HTTP_201_CREATED)