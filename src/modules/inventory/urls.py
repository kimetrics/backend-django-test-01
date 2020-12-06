from django.urls import path
from .views import ProductView,ProductEdit

urlpatterns = [
    path('products/',ProductView.as_view(), name='product_data'),
    path('products/edit/<int:pk>/',ProductEdit.as_view(), name='product_edit')
]   