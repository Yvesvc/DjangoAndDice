import json
from django.http import HttpResponse
from django.shortcuts import render
from .forms import Spells5EForm, MetadataForm
from .models import spells_metadata, My_Spells, Spells5E
from users.models import User_Extended
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict

@login_required
def index(request):
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

    #convert corresponding records from Spells5E to list of dictionaries
    my_spells_in_Spells5E_list_of_dict = list(my_spells_in_Spells5E.values())

    #convert user's records of my_spells to list of dictionaries
    my_spells_user_list_of_dict = list(my_spells_user.values())

    #create new list of dictionaries that is join of my_spells and Spells5E
    my_spells_user_and_Spells5E =[]
    for my_spell_el in my_spells_user_list_of_dict:
        for Spells5E_el in my_spells_in_Spells5E_list_of_dict:
            if my_spell_el.get('name') == Spells5E_el.get('name'):
                temp_dict = Spells5E_el
                temp_dict['prepared'] = my_spell_el.get('prepared')
                #create spell_name_id for HTML id attribute
                temp_dict['spell_name_id'] = my_spell_el.get('name').replace(' ', '_').replace('\'', '_').lower()
                my_spells_user_and_Spells5E.append(temp_dict)



    return render (request, 'spells/spells.html', {'Spells5Eform':Spells5Eform, 'Metadataform':Metadataform, 'my_spells_user_and_Spells5E':my_spells_user_and_Spells5E })



def addlevel(request):
    if request.is_ajax() and request.method == 'POST':
        name_spell_form = request.POST['name']
        user_name = User_Extended.objects.get(username=request.user.username)
        #if spell already exists, dont re-add it
        try:
            My_Spells.objects.get(username=user_name, name=name_spell_form)
            # return as json
            data = {}
            return HttpResponse(json.dumps(data), content_type='application/json')

        #if spells doesn't exist yet, add
        except My_Spells.DoesNotExist:
            My_Spells.objects.create(
                username = user_name,
                name = name_spell_form
            )
            #retrieve values as list
            spell_added = Spells5E.objects.values_list('name', 'level', 'desc','higher_level', 'range', 'components','material', 'ritual', 'duration', 'concentration', 'casting_time', 'school', 'char_class', 'archetype','domains','patrons','oaths','circles').get(name=name_spell_form)

            #store in dictionary
            spell_added_dict = {}
            spell_added_dict['name'] = spell_added[0]
            spell_added_dict['level'] = spell_added[1]
            spell_added_dict['desc'] = spell_added[2]
            spell_added_dict['higher_level'] = spell_added[3]
            spell_added_dict['range'] = spell_added[4]
            spell_added_dict['components'] = spell_added[5]
            spell_added_dict['material'] = spell_added[6]
            spell_added_dict['ritual'] = spell_added[7]
            spell_added_dict['duration'] = spell_added[8]
            spell_added_dict['concentration'] = spell_added[9]
            spell_added_dict['casting_time'] = spell_added[10]
            spell_added_dict['school'] = spell_added[1]
            spell_added_dict['char_class'] = spell_added[12]
            spell_added_dict['archetype'] = spell_added[13]
            spell_added_dict['domains'] = spell_added[14]
            spell_added_dict['patrons'] = spell_added[15]
            spell_added_dict['oaths'] = spell_added[16]
            spell_added_dict['circles'] = spell_added[17]
            data = spell_added_dict

            #return as json
            return HttpResponse(json.dumps(data), content_type = 'application/json')

def deletelevel(request):
    if request.is_ajax() and request.method == 'POST':
        #Find corresponding record in db and delete
        name_spell= request.POST['spell_name_key']
        user_name = User_Extended.objects.get(username=request.user.username)
        record_to_delete = My_Spells.objects.get(username = user_name, name = name_spell)
        record_to_delete.delete()

        # store name deteled spell in dictionary
        deleted_spell = {}
        deleted_spell['name'] = name_spell
        data = deleted_spell
        #return as json
        return HttpResponse(json.dumps(data), content_type = 'application/json')


def preparationspell(request):
    if request.is_ajax() and request.method == 'POST':
        #Find corresponding record in My_Spells
        name_spell = request.POST['hold_trigger_name_key']
        user_name = User_Extended.objects.get(username=request.user.username)
        spell_to_alter_preparation_status = My_Spells.objects.get(username = user_name, name = name_spell)
        #Update preparation status of spell
        if spell_to_alter_preparation_status.prepared:
            spell_to_alter_preparation_status.prepared = False
        else:
            spell_to_alter_preparation_status.prepared = True
        spell_to_alter_preparation_status.save()
        data= {}

    return HttpResponse(json.dumps(data), content_type='application/json')