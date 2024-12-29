from django.db import models
from django.conf import settings

from vendor.models import Product

class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cart')

    def __str__(self):
        return f"Cart of {self.user.username}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"

    @property
    def total_price(self):
        return self.product.price * self.quantity

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)
    shipping_name = models.CharField(max_length=255)
    shipping_address = models.TextField()
    shipping_phone = models.CharField(max_length=15)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    items = models.ManyToManyField(CartItem, related_name='orders')  

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"