from django.contrib import admin
from .models import *

admin.site.register(Vendor)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Product)