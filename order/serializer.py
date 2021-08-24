from .models import Order, OrderItem
from rest_framework import serializers
from rest_framework.response import Response
from customer.serializer import UserDetailForOrdersSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    product = serializers.ReadOnlyField(source='product.name')

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity']

# Order Serializer that includes user information (username and user_address)


class OrderSerializer(serializers.ModelSerializer):
    order_item = OrderItemSerializer(many=True)
    user = UserDetailForOrdersSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'order_item', 'total', 'accepted', 'user']

# Serializer Create OrderItem


class OrderItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity']

# Serializer Create Order and link to user


class OrderCreateSerializer(serializers.ModelSerializer):
    order_item = OrderItemCreateSerializer(many=True, write_only=True)

    class Meta:
        model = Order
        fields = ['id', 'order_item']

    def create(self, validated_data):
        order = Order.objects.create(user_id=self.context['request'].user.id)
        order_items = validated_data.pop('order_item')
        for item in order_items:
            ordered_item = OrderItem.objects.create(**item)
            order.order_item.add(ordered_item)
        order.total = order.get_total()
        order.save()
        return Response({
            'status': 200,
        })

# Serializer to Update order status


class OrderAcceptedUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['accepted']
