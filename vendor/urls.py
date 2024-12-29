from django.urls import path
from .views import VendorProfileView, VendorDashboardView, AdminDashboardView

urlpatterns = [
    path('profile/', VendorProfileView.as_view(), name='vendor-profile'),
    path('dashboard/', VendorDashboardView.as_view(), name='dashboard'),
    path('admin-dashboard/', AdminDashboardView.as_view(), name='admin-dashboard'),
]

from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, SubcategoryViewSet, ProductViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet),
router.register(r'subcategories', SubcategoryViewSet),
router.register(r'products', ProductViewSet),

urlpatterns += router.urls