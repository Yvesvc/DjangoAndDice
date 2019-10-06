from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    #add column charactername
    charactername = forms.CharField(max_length = 25)

    class Meta:
        #Model want to interact with
        model = User
        #Fields to be shown on form and order
        fields = ['username', 'charactername', 'password1', 'password2']