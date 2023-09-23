from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import *
from django.forms import ModelForm

class RegisterForm(UserCreationForm):
   email = forms.EmailField(required=True)

   class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class Addfile(ModelForm):
    class Meta:
        model=File
        exclude=("usern",)