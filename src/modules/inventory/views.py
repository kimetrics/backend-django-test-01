from django.http import HttpResponseNotAllowed

from rest_framework import viewsets

from .models import Product
from .serializers import ProductSerializer


class ProductApiViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def destroy(self, request, *args, **kwargs):
        return HttpResponseNotAllowed('Method not allowed')
