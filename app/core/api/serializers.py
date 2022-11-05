from rest_framework.serializers import ModelSerializer

from core.models import Products, User


class ProductsSerializer(ModelSerializer):

    class Meta:
        model = Products
        fields = '__all__'


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        exclude = ['groups', 'user_permissions', 'password']


class UserCreateSerializer(ModelSerializer):

    class Meta:
        model = User
        exclude = ['is_superuser', 'is_staff', 'groups', 'user_permissions', 'is_active']
