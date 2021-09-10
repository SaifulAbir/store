from rest_framework import serializers
from products.models import ProductVendor, Product, ProductImage


class ProductVendorSerializer(serializers.ModelSerializer):
    location = serializers.CharField(source='get_location_display')
    vendor = serializers.CharField(source='vendor.name')
    class Meta:
        model = ProductVendor
        fields = ('vendor', 'location', 'price', )


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('image', )


class ProductSerializer(serializers.ModelSerializer):
    vendor_product = ProductVendorSerializer(many=True)
    product_image = ProductImageSerializer(many=True)
    class Meta:
        model = Product
        fields = ('title', 'vendor_product', 'product_image')