from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from .models import Sheet
from .forms import Sheet_Form



@login_required
def index(request):
    #GET request
    if request.method == 'GET':
        #if user already has a record in the database, show form filled with record
        try:
            Sheet_user = Sheet.objects.get(username = request.user.username)
            form = Sheet_Form(instance=Sheet_user)
        # if user already doesn't have a record in the database, show empty form
        except Sheet.DoesNotExist:
            form = Sheet_Form()
    #POST request
    if request.method == 'POST':
        #.copy() to enable to alter the post data
        form = Sheet_Form(request.POST.copy())
        form.data['username'] = request.user.username
        if form.is_valid():
            # delete current record of user if already present
            try: Sheet.objects.get(username=request.user.username).delete()
            except Sheet.DoesNotExist:
                pass
            # save new record of user
            form.save()
        '''
        #debugging: show errors in form validation
        else:
            debugging = str(request.user.username) + str(form.errors) + str(form.non_field_errors)
            return HttpResponse(debugging)
            '''
    return render(request, 'sheet/sheet.html', {'form':form})