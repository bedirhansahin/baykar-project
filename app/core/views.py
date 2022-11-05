from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (
    View,
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,

)
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.messages import constants as messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

from . forms import UserRegisterForm
from . models import Products, User


def error_404_view(request, exception):
    return render(request, '404.html')


class RegisterView(SuccessMessageMixin, CreateView):
    model = User
    template_name = 'register.html'
    success_url = reverse_lazy('core:register')
    form_class = UserRegisterForm
    success_message = "Your profile was created successfully"


class UserEditView(DetailView):
    model = User
    template_name = 'user-detail.html'
    context_object_name = 'user_detail'


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm(request)
    context = {
        "form": form,
    }
    return render(request, "login.html", context)

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("/login/")
    return render(request, "logout.html", {})



class ProductListView(ListView):
    model = Products
    template_name = 'product-list.html'
    context_object_name = 'products'
    paginate_by = 6

    def get_queryset(self):
        search = self.request.GET.get('search', '')
        products = Products.objects.filter(name__icontains=search).order_by(
            '-id'
        )
        return products


class SingleProductView(DetailView):
    model = Products
    template_name = 'single-product.html'
    context_object_name = 'single_product'


class CreateProductView(CreateView):
    model = Products
    template_name = 'create-product.html'
    fields = [
            "producer",
            "name",
            "type",
            "description",
            "date_of_production",
            "weight",
            "image",
        ]
    def get_success_url(self):
        return reverse_lazy('core:single-product', kwargs={'pk': self.object.pk})


class EditProductView(UpdateView):
    model = Products
    template_name = 'edit-product.html'
    fields = '__all__'
    pk_url_kwarg = 'pk'

    def get_success_url(self):
        return reverse_lazy('core:single-product', kwargs={'pk': self.object.pk})


class DeleteProductView(DeleteView):
    model = Products
    pk_url_kwarg = 'pk'
    template_name = 'confirm-delete.html'
    success_url = reverse_lazy('core:products')
