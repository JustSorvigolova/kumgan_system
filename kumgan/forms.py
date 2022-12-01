from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SigninForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Логин'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}))


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]

        widgets = {
            "username": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Логин',
            }),
            "first_name": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя',
            }),
            "last_name": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия',
            }),
            "email": forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'gmail',
            }),
            "password1": forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'password',
            }),
        }
