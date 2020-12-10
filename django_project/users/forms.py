from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.fields import EmailField


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        fields = ['username','email','password1','password2']