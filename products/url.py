from django.urls import path
from .api import ProductListAPIView

urlpatterns = [
    path('', ProductListAPIView.as_view(), name='list'),
]
