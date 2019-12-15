from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import MyEquipment
from .forms import EquipmentForm


@login_required
def index(request):
    #GET request
    if request.method == 'GET':
        #if user already has a record in the database, show form filled with record
        try:
            MyEquipment_user = MyEquipment.objects.get(username = request.user.username)
            form = EquipmentForm(instance=MyEquipment_user)
        # if user already doesn't have a record in the database, show empty form
        except MyEquipment.DoesNotExist:
            form = EquipmentForm()
    #POST request
    if request.method == 'POST':
        #.copy() to enable to alter the post data
        form = EquipmentForm(request.POST.copy())
        form.data['username'] = request.user.username
        if form.is_valid():
            # delete current record of user if already present
            try: MyEquipment.objects.get(username=request.user.username).delete()
            except MyEquipment.DoesNotExist:
                pass
            # save new record of user
            form.save()
        '''
        #debugging: show errors in form validation
        else:
            debugging = str(request.user.username) + str(form.errors) + str(form.non_field_errors)
            return HttpResponse(debugging)
            '''
    return render(request, 'equipment/equipment.html', {'form':form})