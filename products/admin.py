from django.contrib import admin
from products.models import *


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    fields = ['image']
    extra = 2 # how many rows to show


class ProductVendorInline(admin.TabularInline):
    model = ProductVendor
    fields = ['vendor', 'location', 'price']
    extra = 2 # how many rows to show


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = (ProductImageInline, ProductVendorInline)
    list_display = ['title', 'vendor', 'location', 'created_at']

    def vendor(self, obj):
        return ", ".join([vendor_product.vendor.name for vendor_product in obj.vendor_product.all()])

    def location(self, obj):
        return ", ".join([vendor_product.get_location_display() for vendor_product in obj.vendor_product.all()])


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']

