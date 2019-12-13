from django import forms

from .models import MyInfo


general_info_1 = 'width:100%;text-align:center;;font-size:2vh;'
general_info_2 = 'width:100%;height:8.5vh;font-size:1.5vh;'
general_info_3 = 'width:100%;height:14vh;font-size:1.25vh;'

class InfoForm(forms.ModelForm):
    class Meta:
        # Bind Sheet_form to MyInfo Model
        model = MyInfo
        # Enable to display all InfoForm fields in HTML
        fields = '__all__'
        # Add class/id names to InfoForm fields
        widgets = {
         'class_name': forms.TextInput(attrs={'style': general_info_1}),
         'level': forms.NumberInput(attrs={'style': general_info_1}),
         'background': forms.TextInput(attrs={'style': general_info_1}),
         'faction': forms.TextInput(attrs={'style': general_info_1}),
         'race': forms.TextInput(attrs={'style': general_info_1}),
         'alignment': forms.TextInput(attrs={'style': general_info_1}),
         'exp_points': forms.NumberInput(attrs={'style': general_info_1}),
         'dci_number': forms.NumberInput(attrs={'style': general_info_1}),
         'personality_traits': forms.Textarea(attrs={'style': general_info_2}),
         'ideals': forms.Textarea(attrs={'style': general_info_2}),
         'bonds': forms.Textarea(attrs={'style': general_info_2}),
         'flaws': forms.Textarea(attrs={'style': general_info_2}),
         'background_story': forms.Textarea(attrs={'style': general_info_3}),
         'oth_prof_lan': forms.Textarea(attrs={'style': general_info_3}),
         'appearance': forms.Textarea(attrs={'style': general_info_3})
        }