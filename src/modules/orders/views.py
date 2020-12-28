from django.http import HttpResponseNotAllowed
from rest_framework import viewsets

from .serializers import OrderCreateSerializer, OrderListSerializer
from .models import Order


class MultiSerializerModelViewSet(viewsets.ModelViewSet):

    serializers = {
        'default': None
    }

    def get_serializer_class(self):
        return self.serializers.get(
            self.action,
            self.serializers.get('default')
        )


class OrderApiViewSet(MultiSerializerModelViewSet):

    queryset = Order.objects.all()
    serializers = {
        'create': OrderCreateSerializer,
        'default': OrderListSerializer,

    }

    def perform_create(self, serializer):
        self.order = serializer.save()

    def create(self, request, *args, **kwargs):
        resp = super(OrderApiViewSet, self).create(request, *args, **kwargs)
        serializer = OrderListSerializer(instance=self.order)
        resp.data = serializer.data
        return resp

    def destroy(self, request, *args, **kwargs):
        return HttpResponseNotAllowed('Method not allowed')

    def update(self, request, *args, **kwargs):
        return HttpResponseNotAllowed('Method not allowed')
