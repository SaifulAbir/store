from django.db.models import Prefetch
from rest_framework.generics import ListAPIView
from products.models import Product, ProductVendor
from products.serializers import ProductSerializer


class ProductAPI(ListAPIView):
    permission_classes = ()
    serializer_class = ProductSerializer

    def get_queryset(self):
        request = self.request
        location = request.GET.get('location')
        queryset = Product.objects.prefetch_related(Prefetch(
            'vendor_product', queryset=ProductVendor.objects.filter(location = location))).\
            prefetch_related('product_image').filter(vendor_product__location = location)
        return queryset