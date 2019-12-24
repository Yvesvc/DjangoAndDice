from django import forms
from .models import Spells5E, spells_metadata, My_Spells


meta_style = 'width:10vw; text-align:center'
lvl_style = 'width:80%; height:100%;'

class Spells5EForm (forms.ModelForm):
    name = forms.ModelChoiceField(queryset=Spells5E.objects.values_list('name', flat=True), widget=forms.Select(attrs={'style':'font-size:3vw'})) #django automatically assigns id = "id_name"

    class Meta:
        model = Spells5E
        fields = ['name']

class MetadataForm (forms.ModelForm):
    class Meta:
        model = spells_metadata
        fields = ['scability', 'ssdc', 'sabonus', 'username', 'lvl1_total', 'lvl1_left', 'lvl2_total', 'lvl2_left', 'lvl3_total', 'lvl3_left', 'lvl4_total', 'lvl4_left', 'lvl5_total', 'lvl5_left', 'lvl6_total', 'lvl6_left', 'lvl7_total', 'lvl7_left', 'lvl8_total', 'lvl8_left', 'lvl9_total', 'lvl9_left' ]
        widgets = {
            'scability': forms.NumberInput(attrs={'style': meta_style}),
            'ssdc': forms.NumberInput(attrs={'style': meta_style}),
            'sabonus': forms.NumberInput(attrs={'style': meta_style}),
            'lvl1_total': forms.NumberInput(attrs={'style': lvl_style}),
            'lvl1_left': forms.NumberInput(attrs={'style': lvl_style}),
            'lvl2_total': forms.NumberInput(attrs={'style': lvl_style}),
            'lvl2_left': forms.NumberInput(attrs={'style': lvl_style}),
            'lvl3_total': forms.NumberInput(attrs={'style': lvl_style}),
            'lvl3_left': forms.NumberInput(attrs={'style': lvl_style}),
            'lvl4_total': forms.NumberInput(attrs={'style': lvl_style}),
            'lvl4_left': forms.NumberInput(attrs={'style': lvl_style}),
            'lvl5_total': forms.NumberInput(attrs={'style': lvl_style}),
            'lvl5_left': forms.NumberInput(attrs={'style': lvl_style}),
            'lvl6_total': forms.NumberInput(attrs={'style': lvl_style}),
            'lvl6_left': forms.NumberInput(attrs={'style': lvl_style}),
            'lvl7_total': forms.NumberInput(attrs={'style': lvl_style}),
            'lvl7_left': forms.NumberInput(attrs={'style': lvl_style}),
            'lvl8_total': forms.NumberInput(attrs={'style': lvl_style}),
            'lvl8_left': forms.NumberInput(attrs={'style': lvl_style}),
            'lvl9_total': forms.NumberInput(attrs={'style': lvl_style}),
            'lvl9_left': forms.NumberInput(attrs={'style': lvl_style})
        }



class MySpellsForm (forms.ModelForm):
    class Meta:
        model = My_Spells
        fields = ['name']

