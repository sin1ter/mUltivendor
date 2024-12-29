from rest_framework import serializers
from .models import Cart, CartItem, Order

class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'product_name', 'quantity', 'total_price']

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    total_cost = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items', 'total_cost']

    def get_total_cost(self, obj):
        return sum(item.total_price for item in obj.items.all())

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'user', 'shipping_name', 'shipping_address', 'shipping_phone', 'total_cost', 'created_at']
        read_only_fields = ['id', 'user', 'created_at']  # Remove total_cost from read_only_fields

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return super().create(validated_data)