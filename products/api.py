from .models import Product
from rest_framework import generics
from .serializer import ProductSerializer


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all().order_by('-created_on')
    serializer_class = ProductSerializer
