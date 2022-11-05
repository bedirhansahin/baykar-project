from rest_framework import generics, permissions

from core.api.serializers import (
    ProductsSerializer,
    UserSerializer,
    UserCreateSerializer)

from core.models import Products, User


class ProductsListCreateAPIView(generics.ListCreateAPIView):
    queryset = Products.objects.all().order_by('id')
    serializer_class = ProductsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # You can see all UAVs but you can create UAV if you logged in


# UAV Update and Delete API
class ProductsDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = [permissions.IsAdminUser]  # You can Update or Delete if you are an admin.


# User Create API
class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


# User List API
class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]  # You can see all users if you logged in


# User Update and Delete API
class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]  # You can Update or Delete if you are an admin.
