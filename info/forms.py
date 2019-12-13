from django import forms

from .models import MyInfo




class InfoForm(forms.ModelForm):
    class Meta:
        # Bind Sheet_form to MyInfo Model
        model = MyInfo
        # Enable to display all InfoForm fields in HTML
        fields = '__all__'
        # Add class/id names to InfoForm fields
        widgets = {
         'class_name': forms.TextInput(),
         'level': forms.NumberInput(),
         'background': forms.TextInput(),
         'faction': forms.TextInput(),
         'race': forms.TextInput(),
         'alignment': forms.TextInput(),
         'exp_points': forms.NumberInput(),
         'dci_number': forms.NumberInput(),
         'personality_traits': forms.TextInput(),
         'ideals': forms.TextInput(),
         'bonds': forms.TextInput(),
         'flaws': forms.TextInput(),
         'background_story': forms.Textarea(),
         'oth_prof_lan': forms.Textarea(),
         'appearance': forms.Textarea()
        }