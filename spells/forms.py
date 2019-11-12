from django import forms
from .models import Spells5E, spells_metadata

'''
class Spells5EForm(forms.Form):
    spell_name = forms.ModelChoiceField(queryset=Spells5E.objects.values_list('name', flat=True))

'''

meta_style = 'width:10vw; text-align:center'

class Spells5EForm (forms.ModelForm):
    name = forms.ModelChoiceField(queryset=Spells5E.objects.values_list('name', flat=True), widget=forms.Select(attrs={'style':'font-size:3vw'}))

    class Meta:
        model = Spells5E
        fields = ['name']

class MetadataForm (forms.ModelForm):
    class Meta:
        model = spells_metadata
        fields = ['scability', 'ssdc', 'sabonus', 'username']
        widgets = {
            'scability': forms.NumberInput(attrs={'style': meta_style}),
            'ssdc': forms.NumberInput(attrs={'style': meta_style}),
            'sabonus': forms.NumberInput(attrs={'style': meta_style})
        }