from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from modules.inventory.views import ProductApiViewSet
from modules.orders.views import OrderApiViewSet


api_router = DefaultRouter()
api_router.register(r'products', ProductApiViewSet)
api_router.register(r'orders', OrderApiViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_router.urls)),
]
