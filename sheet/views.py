from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import Sheet_Form
from django.contrib.auth.models import User

@login_required
def index(request):
    form = Sheet_Form()
    return render(request, 'sheet/sheet.html', {'form': form})