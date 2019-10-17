from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import Sheet_Form
from django.contrib.auth import get_user_model

@login_required
def index(request):
    User = get_user_model()
    foo = User
    form = Sheet_Form()
    return render(request, 'sheet/sheet.html')