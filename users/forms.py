from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import User_Extended

class UserRegisterForm(UserCreationForm):

    class Meta:
        #Model want to interact with
        model = User_Extended
        #Fields to be shown on form and order
        fields = ['username', 'charactername', 'password1', 'password2']