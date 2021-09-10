from django.urls import path
from products.api import ProductAPI

urlpatterns = [
    path('product/', ProductAPI.as_view()),
]