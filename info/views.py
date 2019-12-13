from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from .models import MyInfo
from .forms import InfoForm


@login_required
def index(request):
    #GET request
    if request.method == 'GET':
        #if user already has a record in the database, show form filled with record
        try:
            Info_user = MyInfo.objects.get(username = request.user.username)
            form = InfoForm(instance=Info_user)
        # if user already doesn't have a record in the database, show empty form
        except MyInfo.DoesNotExist:
            form = InfoForm()
    #POST request
    if request.method == 'POST':
        #.copy() to enable to alter the post data
        form = InfoForm(request.POST.copy())
        form.data['username'] = request.user.username
        if form.is_valid():
            # delete current record of user if already present
            try: MyInfo.objects.get(username=request.user.username).delete()
            except MyInfo.DoesNotExist:
                pass
            # save new record of user
            form.save()
        '''
        #debugging: show errors in form validation
        else:
            debugging = str(request.user.username) + str(form.errors) + str(form.non_field_errors)
            return HttpResponse(debugging)
            '''
    return render(request, 'info/info.html', {'form':form})