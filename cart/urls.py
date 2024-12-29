from django.urls import path
from .views import CartViewSet, CheckoutView

urlpatterns = [
    path('', CartViewSet.as_view({'get': 'retrieve'}), name='cart'),
    path('add/', CartViewSet.as_view({'post': 'add_item'}), name='cart-add'),
    path('remove/<int:pk>/', CartViewSet.as_view({'delete': 'remove_item'}), name='cart-remove'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
]