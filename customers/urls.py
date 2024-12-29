from django.urls import path
from .views import CategoryListAPIView, CategoryRetrieveAPIView, SubcategoryListAPIView, SubcategoryRetrieveAPIView, ProductListAPIView, ProductRetrieveAPIView

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryRetrieveAPIView.as_view(), name='category-detail'),
    path('subcategories/', SubcategoryListAPIView.as_view(), name='subcategory-list'),
    path('subcategories/<int:pk>/', SubcategoryRetrieveAPIView.as_view(), name='subcategory-detail'),
    path('products/', ProductListAPIView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductRetrieveAPIView.as_view(), name='product-detail'),
]
