from order.models import Order
from customer.models import UserAddress
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


# User Address Serializer
class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = ['id', 'address', 'city', 'country', 'postal_code']

# User Detail Serializer


class UserDetailSerializer(serializers.ModelSerializer):
    user_address = UserAddressSerializer()

    class Meta:
        model = User
        fields = ['id', 'email', "username",
                  'first_name', 'last_name', 'user_address']

# User Address and Username for Order Serializer


class UserDetailForOrdersSerializer(serializers.ModelSerializer):
    user_address = UserAddressSerializer()

    class Meta:
        model = User
        fields = ['username', 'user_address']


# User Registration
class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    username = serializers.CharField(write_only=True)
    access = serializers.CharField(allow_blank=True, read_only=True)
    user_address = UserAddressSerializer(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email',
                  "first_name", "last_name", 'access', "user_address"]

    def create(self, validated_data):
        user_address = validated_data.pop('user_address')
        user_address_instance = UserAddress.objects.create(**user_address)
        new_user = User(**validated_data)
        new_user.set_password(validated_data['password'])
        new_user.save()
        user_address_instance.user = new_user
        user_address_instance.save()
        payload = RefreshToken.for_user(new_user)
        payload['username'] = new_user.username
        token = str(payload.access_token)
        return {'access': token}



# User SignIn

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['admin'] = user.is_staff
        return token
