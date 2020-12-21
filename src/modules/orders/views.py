import json
from .models import Order
from rest_framework import status
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import SerializedOrder

class OrdersList( APIView ):
    def get( self, request ):
        orders = Order.objects.all()
        serialized_orders = SerializedOrder( orders, many= True )
        print ("////////////////////////////////LISTANDO  ORDENES////////////////////////////////")
        print( serialized_orders.data )
        return Response(serialized_orders.data, status=status.HTTP_200_OK)

class CreateOrder( APIView ):
    def post( self, request ):
        try:
            serialized_order = SerializedOrder( request.data )
            if serialized_order.is_valid():
                print ("////////////////////////////////CREANDO  ORDEN////////////////////////////////")
                print (serialized_order)
                serialized_order.save()
                json_orden = json.dumps(serialized_order.data)
                print (json_orden)
                return Response( json_orden, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"Status":"BAD", "End": e},status= 405)

class RetrieveOrder( APIView ):
    def get( self, request, id ):
        try:
            order = Order.objects.get(id=id)
            serialized_order = SerializedOrder( order, many= False )
            print ("////////////////////////////////OBTENIENDO  ORDEN////////////////////////////////")
            print(serialized_order.data)
            return Response( serialized_order.data, status=status.HTTP_200_OK )
        except Exception as e:
            return Response({"Status":"BAD", "End": e},status= 405)

class UpdateOrder( APIView ):
    def put( self, request, id ):
        print ("////////////////////////////////PUT ACTUALIZACIÓN NO AUTORIZADA ORDEN////////////////////////////////")
        return Response(status= 405)
    def patch( self, request, id ):
        print ("////////////////////////////////PATCH ACTUALIZACIÓN NO AUTORIZADA ORDEN////////////////////////////////")
        return Response(status= 405)

class DeleteOrder( APIView ):
    def delete( self, request, id ):
        print ("////////////////////////////////ELIMINACIÓN NO AUTORIZADA ORDEN////////////////////////////////")
        return Response(status= 405)
