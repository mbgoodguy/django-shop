<<<<<<< HEAD
from rest_framework.generics import ListAPIView

from products.models import Product
from products.serializers import ProductSerializer


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
=======
from django.shortcuts import render

# Create your views here.
>>>>>>> a8f2e6ec69e56fd474ddfe70a026a7ec11383144
