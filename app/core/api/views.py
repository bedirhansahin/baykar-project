from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404

from core.api.serializers import ProductsSerializer, UserSerializer, UserCreateSerializer
from core.api.permissions import IsAdminUserOrReadOnly

from core.models import Products, Type, User



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