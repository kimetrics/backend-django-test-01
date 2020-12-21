from django.urls import path, include
from .views import *
from django.conf.urls.static import static

urlpatterns = [
    path('', ProductsList.as_view(), name="products_list"),
    path('create/', CreateProduct.as_view(), name="create_product"),
    path('retrieve/<str:id>/', RetrieveProduct.as_view(), name="retrieve_product"),
    path('update/<str:id>/', UpdateProduct.as_view(), name="update_product"),
    path('delete/<str:id>/', DeleteProduct.as_view(), name="delete_product"),
] 