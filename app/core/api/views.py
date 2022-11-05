from rest_framework import generics, permissions

from core.api.serializers import (
    ProductsSerializer,
    UserSerializer,
    UserCreateSerializer)

from core.models import Products, User


class ProductsListCreateAPIView(generics.ListCreateAPIView):
    queryset = Products.objects.all().order_by('id')
    serializer_class = ProductsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ProductsDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = [permissions.IsAdminUser]


class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]
