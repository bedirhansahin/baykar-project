from django.urls import path

from core.api import views as api_views

urlpatterns = [
    path('user-create/', api_views.UserCreateAPIView.as_view(), name='api-create-user'),  # To create a new user endpoint
    path('user-list/', api_views.UserListAPIView.as_view(), name='api-users'),  # To list all users
    path('user/<int:pk>', api_views.UserDetailAPIView.as_view(), name='api-user-detail'),  # To list only user you want
    path('product-list/', api_views.ProductsListCreateAPIView.as_view(), name='api-products'),  # To list all UAVs
    path('product/<int:pk>', api_views.ProductsDetailAPIView.as_view(), name='api-product-detail'),  # To list only UAV you want
]
