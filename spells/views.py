from django.http import HttpResponse
from django.shortcuts import render
from .forms import Spells5EForm

def index (request):
    if request.method == 'GET':
        Spells5Eform = Spells5EForm()
    if request.method == 'POST':
        return HttpResponse('added (but not actually) ')
    return render (request, 'spells/spells.html', {'Spells5Eform':Spells5Eform})