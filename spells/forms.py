from django import forms
from .models import Spells5E

'''
class Spells5EForm(forms.Form):
    spell_name = forms.ModelChoiceField(queryset=Spells5E.objects.values_list('name', flat=True))

'''



class Spells5EForm (forms.ModelForm):
    name = forms.ModelChoiceField(queryset=Spells5E.objects.values_list('name', flat=True), widget=forms.Select(attrs={'style':'font-size:3vw'}))

    class Meta:
        model = Spells5E
        fields = ['name']