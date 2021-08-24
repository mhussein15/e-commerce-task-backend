from customer.models import UserAddress
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from .serializer import UserCreateSerializer, UserDetailSerializer
from .serializer import MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.response import Response


# Register User
class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer

# SignIn


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

# Get User Detail


class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        user = User.objects.get(id=self.request.user.id)
        serializer = UserDetailSerializer(user)
        return Response(serializer.data)
