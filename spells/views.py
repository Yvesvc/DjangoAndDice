from django.http import HttpResponse
from django.shortcuts import render
from .forms import Spells5EForm, MetadataForm
from .models import spells_metadata


def index (request):
    #GET
    if request.method == 'GET':
        if request.method == 'GET':
            # if user already has a record in the database, show form filled with record
            try:
                spells_metadata_user = spells_metadata.objects.get(username=request.user.username)
                Metadataform = MetadataForm(instance=spells_metadata_user)
            # if user already doesn't have a record in the database, show empty form
            except spells_metadata.DoesNotExist:
                Metadataform = MetadataForm()
            # Spells5EForm not linked to user
            Spells5Eform = Spells5EForm()

    #POST
    if request.method == 'POST':

        #Spells5Eform
        if 'btnSpells5Eform' in request.POST:
            return HttpResponse('add spell test')

        #metadataform
        elif 'btnmetadataform' in request.POST:
            # .copy() to enable to alter the post data
            Metadataform = MetadataForm(request.POST.copy())
            Metadataform.data['username'] = request.user.username
            if Metadataform.is_valid():
                # delete current record of user if already present
                try:
                    spells_metadata.objects.get(username=request.user.username).delete()
                except spells_metadata.DoesNotExist:
                    pass
                # save new record of user
                Metadataform.save()
        Spells5Eform = Spells5EForm()

    return render (request, 'spells/spells.html', {'Spells5Eform':Spells5Eform, 'Metadataform':Metadataform })





