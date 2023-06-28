from django.contrib import admin
from product.models import Brand, Category, Product, ProductLine


class ProductLineInLine(admin.TabularInline):
    model = ProductLine


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductLineInLine]


admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(ProductLine)
