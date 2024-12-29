from django.urls import path
from .views import VendorProfileView, VendorDashboardView

urlpatterns = [
    path('profile/', VendorProfileView.as_view(), name='vendor-profile'),
    path('dashboard/', VendorDashboardView.as_view(), name='dashboard'),
]

from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, SubcategoryViewSet, ProductViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet),
router.register(r'subcategories', SubcategoryViewSet),
router.register(r'products', ProductViewSet),

urlpatterns += router.urls