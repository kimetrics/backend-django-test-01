from django.urls import path
from .views import OrderView,OrderEdit

urlpatterns = [
    path('orders/',OrderView.as_view(), name='order_data'),
    path('orders/<int:pk>',OrderEdit.as_view(), name='order_edit'),
]