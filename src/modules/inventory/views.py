from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializers

# Create your views here.
class ProductViewsets(viewsets.ModelViewSet):
    http_method_names = ['get', 'post','put','patch']
    queryset=Product.objects.all()
    serializer_class=ProductSerializers

class ProductViewsetsByName(viewsets.ModelViewSet):
    lookup_field = 'description'
    http_method_names = ['get']
    queryset=Product.objects.all()
    serializer_class=ProductSerializers

    def retrieve(self, request, description=None):
        queryset = Product.objects.all()
        product = get_object_or_404(queryset, description=description)
        serializer = ProductSerializers(product)
        return Response(serializer.data)
