from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','password1','password2'] 
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control form-control-lg"}),
            "password1": forms.TextInput(attrs={"class": "form-control form-control-lg"}),
            "password2": forms.TextInput(attrs={"class": "form-control form-control-lg"})
        }