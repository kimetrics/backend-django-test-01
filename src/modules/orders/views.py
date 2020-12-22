from decimal import Decimal
from .models import Order
from modules.inventory.models import Product
from rest_framework import status
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import SerializedOrder


class OrdersList(APIView):
    def get(self, request):
        orders = Order.objects.all()
        serialized_orders = SerializedOrder(orders, many=True)
        print("////////////////////////////////LISTANDO  ORDENES////////////////////////////////")
        return Response(serialized_orders.data, status=status.HTTP_200_OK)


def create_order(data):
    try:
        items_init = data['items']
        total = 0
        order = {
            'items': [],
            'total': 0
            }
        for prod in items_init:
            item = {}
            quantity = float(prod["quantity"])
            product = Product.objects.get( id = prod[ "id" ] )
            if product.stock >= quantity:
                unit_price = float(product.unit_price)
                total_item = quantity * unit_price
                total = total + total_item
                item = {
                        'description': product.description,
                        'quantity': prod["quantity"],
                        'unit_price': unit_price,
                        'total': total_item
                        }
                order["items"].append(item)
                product.stock = product.stock - quantity
                product.save()
            order['total'] = round(total, 2)
        return order
    except Exception as error:
        return {
                'items': [],
                'total': 0,
                'error' : error
            }

class CreateOrder(APIView ):
    def post(self, request ):
        print("////////////////////////////////CREANDO  ORDEN////////////////////////////////")
        try:
            d = request.data
            order = create_order( d )
            total = order['total']
            items = order['items']
            if total > 0:
                order_s = Order(
                                items = items,
                                total = total
                                )
                order_s.save()
                return Response({
                                'id' : order_s.id,
                                'items' : order_s.items,
                                'total': order_s.total
                                },
                                    status = status.HTTP_200_OK)
        except Exception as e:
            return Response({ "Status" : "BAD", "End" : e }, status = 405 )

    
class RetrieveOrder(APIView ):
    def get(self, request, id ):
        try:
            order = Order.objects.get(id=id)
            print("////////////////////////////////OBTENIENDO  ORDEN////////////////////////////////")
            order_r = {
                    'id' : order.id,
                    'items' : order.items,
                    'total': order.total
                    }
            return Response(order_r,
                            status = status.HTTP_200_OK
                            )
        except Exception as e:
            return Response({"Status": "BAD", "End": e},status= 405)

class UpdateOrder(APIView ):
    def put(self, request, id ):
        print("////////////////////////////////PUT ACTUALIZACIÓN NO AUTORIZADA ORDEN////////////////////////////////")
        return Response(status=405)
    def patch(self, request, id ):
        print("////////////////////////////////PATCH ACTUALIZACIÓN NO AUTORIZADA ORDEN////////////////////////////////")
        return Response(status=405)

class DeleteOrder(APIView ):
    def delete(self, request, id ):
        print("////////////////////////////////ELIMINACIÓN NO AUTORIZADA ORDEN////////////////////////////////")
        return Response(status=405)
