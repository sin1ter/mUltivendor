from decimal import Decimal
from django.db import transaction
from rest_framework import viewsets, status, exceptions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from vendor.models import Product
from .models import Cart, CartItem, Order
from .serializers import CartSerializer, CartItemSerializer, OrderSerializer
from accounts.permissions import IsCustomerOrVendorAdminReadOnly

class CartViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def retrieve(self, request):
        cart, created = Cart.objects.get_or_create(user=request.user)
        serializer = CartSerializer(cart)
        return Response(serializer.data)

    def add_item(self, request):
        user=request.user
        print(user.role)
        cart, created = Cart.objects.get_or_create(user=request.user)
        product_id = request.data.get('product')
        quantity = int(request.data.get('quantity', 1))

        if not product_id:
            raise exceptions.ValidationError({"detail": "Please select at least one product."})

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            raise exceptions.ValidationError({"detail": "The selected product does not exist."})

        # Add or update CartItem
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            cart_item.quantity += quantity
        cart_item.save()

        serializer = CartItemSerializer(cart_item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def remove_item(self, request, pk=None):
        cart = Cart.objects.get(user=request.user)
        cart_item = CartItem.objects.get(cart=cart, id=pk)
        cart_item.delete()
        return Response({"detail": "Item removed."}, status=status.HTTP_204_NO_CONTENT)


class CheckoutView(APIView):
    permission_classes = [IsAuthenticated]

    @transaction.atomic
    def post(self, request):
        try:
            cart = Cart.objects.get(user=request.user)
        except Cart.DoesNotExist:
            return Response({"detail": "Cart not found."}, status=status.HTTP_400_BAD_REQUEST)

        if not cart.items.exists():
            return Response({"detail": "Cart is empty."}, status=status.HTTP_400_BAD_REQUEST)

        total_cost = Decimal('0.00')
        for item in cart.items.all():
            total_cost += Decimal(str(item.total_price))
        
        print(f"Total cost calculated: {total_cost}")  

        order_data = {
            'shipping_name': request.data.get('shipping_name'),
            'shipping_address': request.data.get('shipping_address'),
            'shipping_phone': request.data.get('shipping_phone'),
            'total_cost': total_cost,
        }

        serializer = OrderSerializer(data=order_data, context={'request': request})
        if serializer.is_valid():
            order = serializer.save()
            cart.items.all().delete()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    