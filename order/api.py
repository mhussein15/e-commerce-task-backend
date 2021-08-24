from .models import Order, OrderItem
from rest_framework import generics
from .serializer import OrderSerializer, OrderCreateSerializer, OrderItemSerializer, OrderAcceptedUpdateSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

# Get Orders List


class OrderListAPIView(generics.ListAPIView):
    queryset = Order.objects.all().order_by('-created_on')
    serializer_class = OrderSerializer
    permission_classes = [IsAdminUser]

# Get Current User Orders List


class OrderUserAPIView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by('-created_on')

# Create Order


class OrderCreateAPIView(generics.CreateAPIView):
    serializer_class = OrderCreateSerializer
    permission_classes = [IsAuthenticated]

# Update Order Status


class OrderUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderAcceptedUpdateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'
    permission_classes = [IsAdminUser]
