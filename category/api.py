from .models import Category
from rest_framework import generics
from .serializer import CategorySerializer

# Return Category List
class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
