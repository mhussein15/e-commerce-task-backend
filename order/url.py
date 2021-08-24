from django.urls import path
from .api import OrderListAPIView, OrderCreateAPIView, OrderUpdateView

urlpatterns = [
    path('', OrderListAPIView.as_view(), name='list'),
    path('add', OrderCreateAPIView.as_view(), name='add'),
    path('<int:object_id>', OrderUpdateView.as_view(), name='update'),
]
