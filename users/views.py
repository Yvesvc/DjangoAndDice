from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

#Register
def register(request):
    #POST
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Your account has successfully been created!')
            return redirect ('login')
    #GET
    else:
        form = UserRegisterForm()
    return render(request, 'users/registration.html', {'form': form})

#Login
def login(request):
    return render (request, 'users/login.html')