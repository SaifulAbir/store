from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.


LOCATION_CHOICES = (
    ("dhaka", _("Dhaka")),
    ("rajshahi", _("Rajshahi")),
    ("sylhet", _("Sylhet")),
    ("chattogram", _("Chattogram"))
)


class Product(models.Model):
    title = models.CharField(_('Title'), max_length=255, null=False, blank=False)
    created_at = models.DateTimeField(_('Created'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated'), auto_now=True)

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    """
        image: one to many relation
    """
    image = models.ImageField(upload_to='images', null=True, blank=True)
    Product = models.ForeignKey(
        Product, related_name='product_image',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        verbose_name='Product ID'
    )
    created_at = models.DateTimeField(_('Created'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated'), auto_now=True)


class Vendor(models.Model):
    name = models.CharField(_('Name'), max_length=255, null=False, blank=False)
    created_at = models.DateTimeField(_('Created'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated'), auto_now=True)

    def __str__(self):
        return self.name


class ProductVendor(models.Model):
    vendor = models.ForeignKey(
        Vendor, related_name='product_vendor',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        verbose_name='Vendor'
    )
    location = models.CharField(
        choices=LOCATION_CHOICES,
        max_length=50,
        null=False, blank=False,
        verbose_name='Location'
    )
    product = models.ForeignKey(
        Product, related_name='vendor_product',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        verbose_name='Product ID'
    )
    price = models.DecimalField(_('Price'), max_digits=19, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(_('Created'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated'), auto_now=True)

    def __str__(self):
        return self.vendor.name

