from django.urls import path
from .api import CategoryListAPIView

urlpatterns = [
    path('', CategoryListAPIView.as_view(), name='list'),
]
