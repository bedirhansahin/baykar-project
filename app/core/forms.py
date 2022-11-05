from django import forms
from . models import Products
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from . models import User


# Model form codes for the create or update a UAV
class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = [
            "producer",
            "name",
            "type",
            "description",
            "date_of_production",
            "weight",
            "image",
        ]
        widgets = {
            'date_of_production': forms.TextInput(
                attrs={'placeholder': 'YYYY-DD-MM'})
        }


# Model Form codes to register
class UserRegisterForm(UserCreationForm):
  email = forms.EmailField()

  class Meta:
      model = User
      fields = ['email', 'name']
      widgets = {
        'email': forms.TextInput(attrs={'placeholder': 'example.example.com'})
      }


# Model Form codes to login
class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['email', 'password']
        widgets = {
            'email': forms.TextInput(
                attrs={'placeholder': 'example@example.com'}),
            'password': forms.TextInput(
                attrs={'placeholder': 'Password'})
        }
