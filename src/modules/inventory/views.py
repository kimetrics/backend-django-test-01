from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.forms import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
import json
from .models import Product
from .serializers import ProductSerializer

# Create your views here.
class ProductView(APIView):

    serializer_class = ProductSerializer

    def get(self, request, format=None):
        if ('id' in request.GET):
            data = Product.objects.filter(id__contains=request.GET['id'])
        else:
            data = Product.objects.all()

        return Response(data.values())
    
   
    def post(self, request):
        
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            description = serializer.validated_data.get('description')
            unit_price = serializer.validated_data.get('unit_price')
            stock = serializer.validated_data.get('stock')         
            record = Product(description=description,\
                             unit_price=unit_price,stock=stock)
            record.save()
            return Response({'description':description,'unit_price':unit_price,'stock':stock},\
                            status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,\
                status=status.HTTP_400_BAD_REQUEST)

    
class ProductEdit(APIView):

    serializer_class = ProductSerializer

    def get(self, request, pk):
        data = Product.objects.get(pk=pk)
        return Response(model_to_dict(data))  

    def put(self, request, pk):
        
        try: 
            product = Product.objects.get(pk=pk) 
        except Product.DoesNotExist: 
            return Response({'message': 'The product does not exist'},\
                                status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.serializer_class(product, data=request.data)
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_200_OK) 
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
                   
        serializer = ProductSerializer(Product.objects.get(pk=pk),\
                                        data=request.data, partial=True)
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_200_OK) 
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

