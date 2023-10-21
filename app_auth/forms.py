from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"class": "form-control form-control-lg"}),
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={"class": "form-control form-control-lg"}),
        strip=False,
        help_text="Enter the same password as before, for verification.",
    )

    class Meta:
        model=User
        fields = ['username','password1','password2'] 
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control form-control-lg"}),
        }
