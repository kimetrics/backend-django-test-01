from rest_framework import routers
from .views import ProductViewsets, ProductViewsetsByName
from django.urls import path, include

router = routers.DefaultRouter()
router.register('products',ProductViewsets)
router.register('productByDescription', ProductViewsetsByName)

urlpatterns = [
    path('api/', include(router.urls)),
]