from django.db.models import Sum
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, viewsets, response, status, views
from .models import Vendor, Category, Subcategory, Product
from .serializers import VendorSerializer, CategorySerializer, SubcategorySerializer, ProductSerializer
from accounts.permissions import IsVendor, IsAdmin, IsVendorOrAdminOrReadOnly
from cart.models import Order
from accounts.models import CustomUser

class VendorProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = VendorSerializer
    permission_classes = [permissions.IsAuthenticated, IsVendor]

    def get_object(self):
        vendor, created = Vendor.objects.get_or_create(user=self.request.user)
        return vendor



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated, IsVendorOrAdminOrReadOnly]


class SubcategoryViewSet(viewsets.ModelViewSet):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer
    permission_classes = [permissions.IsAuthenticated, IsVendorOrAdminOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        print(user)
        return Subcategory.objects.all()


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['vendor', 'category', 'subcategory', 'price']

    def get_queryset(self):
        user = self.request.user
        if user.role == 'vendor':
            return Product.objects.filter(vendor=user.vendor_profile)
        elif user.role == 'admin':
            return Product.objects.all()
        elif user.role == 'customers':
            return Product.objects.all()
        return Product.objects.none()

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(vendor=user.vendor_profile)
    

class VendorDashboardView(views.APIView):
    permission_classes = [permissions.IsAuthenticated, IsVendor]

    def get(self, request):
        if request.user.role != 'vendor':
            return response.Response({"detail": "You do not have permission to view this data."}, status=status.HTTP_403_FORBIDDEN)

        total_products = Product.objects.filter(vendor=request.user.vendor_profile).count()

        orders = Order.objects.filter(user=request.user).all()
        total_orders = orders.count()

        total_revenue = orders.aggregate(Sum('total_cost'))['total_cost__sum'] or 0.00

        analytics_data = {
            "total_products": total_products,
            "total_orders": total_orders,
            "total_revenue": total_revenue
        }

        return response.Response(analytics_data, status=status.HTTP_200_OK)
    
class AdminDashboardView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        if request.user.role != 'admin':
            return response.Response({"detail": "You do not have permission to view this data."}, status=status.HTTP_403_FORBIDDEN)

        total_vendors = CustomUser.objects.filter(role='vendor').count()

        total_products = Product.objects.all().count()

        total_orders = Order.objects.all().count()

        total_revenue = Order.objects.aggregate(Sum('total_cost'))['total_cost__sum'] or 0.00

        analytics_data = {
            "total_vendors": total_vendors,
            "total_products": total_products,
            "total_orders": total_orders,
            "total_revenue": total_revenue
        }

        return response.Response(analytics_data, status=status.HTTP_200_OK)
    

class VendorManagementViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated, IsAdmin]

    def list(self, request):
        vendors = CustomUser.objects.filter(role='vendor')
        serializer = VendorSerializer(vendors, many=True)
        return response.Response(serializer.data)

    def update(self, request, pk=None):
        try:
            vendor = CustomUser.objects.get(id=pk, role='vendor')
        except CustomUser.DoesNotExist:
            return response.Response({"detail": "Vendor not found."}, status=status.HTTP_404_NOT_FOUND)

        vendor.is_active = request.data.get('is_active', vendor.is_active)  
        vendor.save()
        return response.Response({"detail": "Vendor status updated."}, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        try:
            vendor = CustomUser.objects.get(id=pk, role='vendor')
        except CustomUser.DoesNotExist:
            return response.Response({"detail": "Vendor not found."}, status=status.HTTP_404_NOT_FOUND)

        vendor.delete()
        return response.Response({"detail": "Vendor deleted."}, status=status.HTTP_204_NO_CONTENT)