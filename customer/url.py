from customer.serializer import UserDetailSerializer
from django.urls import path
from .api import UserCreateAPIView, UserDetailView, MyTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from order.api import OrderUserAPIView

urlpatterns = [
    path('signup', UserCreateAPIView.as_view(), name='signup'),
    path('signin', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('order', OrderUserAPIView.as_view(), name='order'),
    path('detail', UserDetailView.as_view(), name='address'),
]
