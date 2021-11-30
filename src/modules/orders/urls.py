from rest_framework import routers
from .views import OrderViewsets
from django.urls import path, include

router = routers.DefaultRouter()
router.register('orders',OrderViewsets)

urlpatterns = [
    path('api/', include(router.urls)),
]