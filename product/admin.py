from django.contrib import admin
from product.models import Brand, Category, Product

admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(Category)
