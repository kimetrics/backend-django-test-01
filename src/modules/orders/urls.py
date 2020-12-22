from django.urls import path, include
from .views import *
from django.conf.urls.static import static

urlpatterns = [
    path('', OrdersList.as_view(), name="orders_list"),
    path('create/', CreateOrder.as_view(), name="create_order"),
    path('retrieve/<str:id>/', RetrieveOrder.as_view(), name="retrieve_order"),
    path('update/<str:id>/', UpdateOrder.as_view(), name="update_order"),
    path('delete/<str:id>/', DeleteOrder.as_view(), name="delete_order"),
] 