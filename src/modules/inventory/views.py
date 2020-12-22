from .models import Product
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import SerializedProduct

class ProductsList( APIView ):
    def get( self, request ):
        try:
            products = Product.objects.all()
            serialized_products = SerializedProduct( products, many = True )
            print ( "////////////////////////////////LISTANDO  PRODUCTOS////////////////////////////////" )
            return Response( serialized_products.data, status = status.HTTP_200_OK )
        except Exception as e:
            return Response( { "Status" : "BAD", "End" : e }, status = 405 )

class CreateProduct( APIView ):
    def post( self, request ):
        try:
            serialized_product = SerializedProduct( data = request.data )
            if serialized_product.is_valid():
                print ("////////////////////////////////CREANDO  PRODUCTO////////////////////////////////")
                description = serialized_product.validated_data.get('description')
                unit_price = serialized_product.validated_data.get('unit_price')
                stock = serialized_product.validated_data.get('stock')         
                product = Product( 
                                    description = description, 
                                    unit_price = unit_price, 
                                    stock = stock 
                                )
                product.save()
                return Response({ 
                                    'id' : product.id, 
                                    'description' : description, 
                                    'unit_price' : str(unit_price), 
                                    'stock' : stock 
                                },
                                status = status.HTTP_200_OK )
        except Exception as e:
            return Response( { "Status" : "BAD", "End" : e }, status = 405 )
        

class RetrieveProduct( APIView ):
    def get( self, request, id ):
        try:
            product = Product.objects.get( id = id )
            serialized_product = SerializedProduct( product, many = False )
            print ( "////////////////////////////////OBTENIENDO  PRODUCTO////////////////////////////////" )
            return Response( serialized_product.data, status = status.HTTP_200_OK )
        except Exception as e:
            return Response( { "Status" : "BAD", "End" : e },status = 405 )


class UpdateProduct( APIView ):
    def put( self, request, id ):
        try:
            product = Product.objects.get( id = id )
            serialized_product = SerializedProduct( product, request.data )
            if serialized_product.is_valid():
                print ( "////////////////////////////////PUT ACTUALIZANDO  PRODUCTO////////////////////////////////" )
                serialized_product.save()
                return Response( serialized_product.data, status = status.HTTP_200_OK )
        except Exception as e:
            return Response( { "Status" : "BAD", "End" : e }, status = 405 )

    def patch( self, request, id ):
        try:
            product = Product.objects.get( id = id )
            serialized_product = SerializedProduct( product, data = request.data, partial = True )
            if serialized_product.is_valid():
                print ( "////////////////////////////////PATCH ACTUALIZANDO  PRODUCTO////////////////////////////////" )
                serialized_product.save()
                return Response( serialized_product.data, status = status.HTTP_200_OK )
        except Exception as e:
            return Response( { "Status" : "BAD", "End" : e }, status = 405 )


class DeleteProduct( APIView ):
    def delete( self, request, id ):
        print ( "////////////////////////////////ELIMINACIÓN NO AUTORIZADA PRODUCTO////////////////////////////////" )
        return Response( status = 405 )
