from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'admin'

class IsVendor(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'vendor'

class IsCustomer(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'customer'
    

class IsVendorOrAdminOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return request.user.is_authenticated and request.user.role == 'customer'

        return request.user.is_authenticated and (request.user.role == 'vendor' or request.user.role == 'admin')
    

class IsCustomerOrVendorAdminReadOnly(BasePermission):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return request.user.is_authenticated and (request.user.role == 'vendor' or request.user.role == 'admin')

        return request.user.is_authenticated and request.user.role == 'customer'

