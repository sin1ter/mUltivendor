from rest_framework import serializers
from .models import Vendor, Category, Subcategory, Product

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['id', 'name', 'phone', 'address', 'user']
        read_only_fields = ['id', 'user']

    def create(self, validated_data):
        user = self.context['request'].user
        return Vendor.objects.create(user=user, **validated_data)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ['id', 'name', 'category']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id', 'name', 'description', 'price', 'stock_quantity', 
            'category', 'subcategory', 'vendor'
        ]
        read_only_fields = ['id', 'vendor']
