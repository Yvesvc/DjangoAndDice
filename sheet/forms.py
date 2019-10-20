from django import forms

from .models import Sheet

class Sheet_Form(forms.ModelForm):

    class Meta:
        #Bind Sheet_form to Sheet Model
        model = Sheet
        #Enable to display all Sheet_form fields in HTML
        fields = '__all__'
        #Add class/id names to Sheet_forn fields
        widgets = {
            'level': forms.NumberInput(attrs = {'style': 'width:20%; text-align:center'}),

            #Attributes
            'strength': forms.NumberInput(attrs={'style': 'width:50%; text-align:center'}),
            'strength_mod': forms.NumberInput(attrs={'style': 'width:25%; text-align:center'}),
            'dexterity': forms.NumberInput(attrs={'style': 'width:50%; text-align:center'}),
            'dexterity_mod': forms.NumberInput(attrs={'style': 'width:25%; text-align:center'}),
            'constitution': forms.NumberInput(attrs={'style': 'width:50%; text-align:center'}),
            'constitution_mod': forms.NumberInput(attrs={'style': 'width:25%; text-align:center'}),
            'intelligence': forms.NumberInput(attrs={'style': 'width:50%; text-align:center'}),
            'intelligence_mod': forms.NumberInput(attrs={'style': 'width:25%; text-align:center'}),
            'wisdom': forms.NumberInput(attrs={'style': 'width:50%; text-align:center'}),
            'wisdom_mod': forms.NumberInput(attrs={'style': 'width:25%; text-align:center'}),
            'charisma': forms.NumberInput(attrs={'style': 'width:50%; text-align:center'}),
            'charisma_mod': forms.NumberInput(attrs={'style': 'width:25%; text-align:center'}),

            #Ins_pro
            'inspiration': forms.NumberInput(attrs={'style': 'width:50%; text-align:center'}),
            'proficiency': forms.NumberInput(attrs={'style': 'width:50%; text-align:center'}),

            #Saving
            'sav_strength_circ': forms.CheckboxInput(attrs={}),
            'sav_strength': forms.NumberInput(attrs={'style': 'width:5vw; text-align:center'}),
            'sav_dexterity_circ': forms.CheckboxInput(attrs={}),
            'sav_dexterity': forms.NumberInput(attrs={'style': 'width:50%; text-align:center'}),
            'sav_constitution_circ': forms.CheckboxInput(attrs={}),
            'sav_constitution': forms.NumberInput(attrs={'style': 'width:50%; text-align:center'}),
            'sav_intelligence_circ': forms.CheckboxInput(attrs={}),
            'sav_intelligence': forms.NumberInput(attrs={'style': 'width:50%; text-align:center'}),
            'sav_wisdom_circ': forms.CheckboxInput(attrs={}),
            'sav_wisdom': forms.NumberInput(attrs={'style': 'width:50%; text-align:center'}),
            'sav_charisma_circ': forms.CheckboxInput(attrs={}),
            'sav_charisma': forms.NumberInput(attrs={'style': 'width:50%; text-align:center'})
        }