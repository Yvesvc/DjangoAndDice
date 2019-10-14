from django import forms

from .models import Sheet

class Sheet_Form(forms.ModelForm):

    class Meta:
        model = Sheet
        fields = '__all__'