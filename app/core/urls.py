from django.urls import path
from . views import (
    ProductListView,
    SingleProductView,
    CreateProductView,
    EditProductView,
    DeleteProductView,
    RegisterView,
    UserEditView,
    login_view,
    logout_view
)

app_name = 'core'

urlpatterns = [
    path('', ProductListView.as_view(), name='products'),
    path('posts/', CreateProductView.as_view(), name='create-product'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('edit/user/<int:pk>', UserEditView.as_view(), name='edit-user'),
    path('no/<int:pk>/', SingleProductView.as_view(), name='single-product'),
    path('edit/<int:pk>/', EditProductView.as_view(), name='edit-product'),
    path('delete/<int:pk>/', DeleteProductView.as_view(), name='delete-product'),
]
