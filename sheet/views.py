from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Sheet
from .forms import Sheet_Form

from django.contrib.auth import get_user_model

@login_required
def index(request):
    if request.method == 'GET':
        Sheet_user = Sheet.objects.get(username = request.user.id)
        form = Sheet_Form(instance = Sheet_user)
    return render(request, 'sheet/sheet.html', {'form':form})