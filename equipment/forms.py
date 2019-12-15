from django import forms

from .models import MyEquipment

# style
#https://stackoverflow.com/questions/9468153/textarea-with-horizontal-rule
equipment_style = 'height:75vh; font-size:10pt;width:100%;background-attachment: local; background-image:linear-gradient(to right, white 10px, transparent 10px),linear-gradient(to left, white 10px, transparent 10px),repeating-linear-gradient(white, white 30px, #ccc 30px, #ccc 31px, white 31px);line-height: 31px;padding: 8px 10px;'


class EquipmentForm(forms.ModelForm):
    class Meta:
        # Bind Sheet_form to MyEquipment Model
        model = MyEquipment
        # Enable to display all Sheet_form fields in HTML
        fields = '__all__'
        # Add class/id names to EquipmentForm fields
        widgets = {
            'equipment_text': forms.Textarea(attrs={'style': equipment_style})
        }