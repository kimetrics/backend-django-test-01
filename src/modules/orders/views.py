from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.forms import model_to_dict
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
from .models import Order
from .serializers import OrderSerializer

# Create your views here.
class OrderView(APIView):

    serializer_class = OrderSerializer

    def get(self, request, format=None):
        if ('id' in request.GET):
            data = Order.objects.filter(id__contains=request.GET['id'])
        else:
            data = Order.objects.all()

        return Response(data.values(), status=status.HTTP_200_OK)
    
    def post(self, request):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            items = serializer.validated_data.get('items')
            total = serializer.validated_data.get('total')         
            record = Order(items=items,total=total)
            record.save()
            return Response({'items':items,'total':total},status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,\
                status=status.HTTP_400_BAD_REQUEST)

class OrderEdit(APIView):

    def get(self, request, pk):
        data = Order.objects.get(pk=pk)
        return Response(model_to_dict(data), status=status.HTTP_200_OK)  