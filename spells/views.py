import json
from django.http import HttpResponse
from django.shortcuts import render
from .forms import Spells5EForm, MetadataForm
from .models import spells_metadata, My_Spells, Spells5E
from users.models import User_Extended


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

        #metadataform
        if 'btnmetadataform' in request.POST:
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


        elif 'btnmetadataform' not in request.POST:
            Metadataform = MetadataForm(request.POST.copy())

        Spells5Eform = Spells5EForm()

    my_spells_user = My_Spells.objects.filter(username=request.user.username)

    #get name of all my_spells and store in list
    my_spells_user_list = []
    for spell in my_spells_user:
        my_spells_user_list.append(spell.name)

    #get all corresponding records from Spells5E
    my_spells_in_Spells5E= Spells5E.objects.filter(name__in=my_spells_user_list)


    #show all those records



    return render (request, 'spells/spells.html', {'Spells5Eform':Spells5Eform, 'Metadataform':Metadataform, 'my_spells_in_Spells5E':my_spells_in_Spells5E })



def addlevel (request):
    if request.is_ajax() and request.method == 'POST':
        name_spell_form = request.POST['name']
        user_name = User_Extended.objects.get(username=request.user.username)
        #name_Spells5E = Spells5E.objects.get(name=name_spell_form)
        My_Spells.objects.create(
            username = user_name,
            name = name_spell_form
        )
        #retrieve values as list
        test = Spells5E.objects.values_list(['level','components'], flat=True).get(name=name_spell_form)
        print(type(test))
        data = {'message': test}
        return HttpResponse(json.dumps(data), content_type = 'application/json')
