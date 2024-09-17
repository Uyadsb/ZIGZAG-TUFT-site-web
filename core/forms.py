from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'style' : 'padding: 0 0 0 10px;background: #ffffff;width: 100%;height: 50px;font-size:17px;background: transparent;outline: none;border: 2px solid black;border-radius:20px'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'style' : 'padding:0 0 0 10px ;background: #ffffff;width: 100%;height: 50px;font-size:17px;background: transparent;outline: none;border: 2px solid black;border-radius:20px'
    }))

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'style' : 'padding:0 0 0 10px ;background: #ffffff;width: 100%;height: 50px;font-size:17px;background: transparent;outline: none;border: 2px solid black;border-radius:20px'
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email address',
        'style' : 'padding:0 0 0 10px ;background: #ffffff;width: 100%;height: 50px;font-size:17px;background: transparent;outline: none;border: 2px solid black;border-radius:20px'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'style' : 'padding:0 0 0 10px ;background: #ffffff;width: 100%;height: 50px;font-size:17px;background: transparent;outline: none;border: 2px solid black;border-radius:20px'
    }))
    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat password',
        'style' : 'padding:0 0 0 10px ;background: #ffffff;width: 100%;height: 50px;font-size:17px;background: transparent;outline: none;border: 2px solid black;border-radius:20px'
    }))