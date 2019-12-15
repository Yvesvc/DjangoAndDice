from django import forms

from .models import Sheet


#style
sav_value = 'width:5vw; text-align:center'
skill_value = 'width:4vw; height:2.5vh; text-align:left;'
attr_std = 'width:50%; text-align:center'
attr_mod = 'width:25%; text-align:center'
ac_init_sp = 'width:8.3vw; height:4vh; text-align:center'
hitp = 'width:24vw; height:6vh; text-align:center'
dice_dth_left = 'width:17vw; height:100%; text-align:center'
dice_dth_right = 'width:8vw; height:100%; text-align:center'
atk_spell = 'width:90%;'
pass_wis = 'width:5vw; height:100%; text-align:center;'
feat_trait = 'height:35vh; font-size:6pt;width:60vw;'


class Sheet_Form(forms.ModelForm):

    class Meta:
        #Bind Sheet_form to Sheet Model
        model = Sheet
        #Enable to display all Sheet_form fields in HTML
        fields = '__all__'
        #Add class/id names to Sheet_form fields
        widgets = {
            'level': forms.NumberInput(attrs = {'style': 'width:30%; text-align:center'}),

            #Attributes
            'strength': forms.NumberInput(attrs={'style': attr_std}),
            'strength_mod': forms.NumberInput(attrs={'style': attr_mod}),
            'dexterity': forms.NumberInput(attrs={'style': attr_std}),
            'dexterity_mod': forms.NumberInput(attrs={'style': attr_mod}),
            'constitution': forms.NumberInput(attrs={'style': attr_std}),
            'constitution_mod': forms.NumberInput(attrs={'style': attr_mod}),
            'intelligence': forms.NumberInput(attrs={'style': attr_std}),
            'intelligence_mod': forms.NumberInput(attrs={'style': attr_mod}),
            'wisdom': forms.NumberInput(attrs={'style': attr_std}),
            'wisdom_mod': forms.NumberInput(attrs={'style': attr_mod}),
            'charisma': forms.NumberInput(attrs={'style': attr_std}),
            'charisma_mod': forms.NumberInput(attrs={'style': attr_mod}),

            #Ins_pro
            'inspiration': forms.NumberInput(attrs={'style': 'width:50%; text-align:center'}),
            'proficiency': forms.NumberInput(attrs={'style': 'width:50%; text-align:center'}),

            #Saving


            'sav_strength_circ': forms.CheckboxInput(attrs={}),
            'sav_strength': forms.NumberInput(attrs={'style': sav_value}),
            'sav_dexterity_circ': forms.CheckboxInput(attrs={}),
            'sav_dexterity': forms.NumberInput(attrs={'style': sav_value}),
            'sav_constitution_circ': forms.CheckboxInput(attrs={}),
            'sav_constitution': forms.NumberInput(attrs={'style': sav_value}),
            'sav_intelligence_circ': forms.CheckboxInput(attrs={}),
            'sav_intelligence': forms.NumberInput(attrs={'style': sav_value}),
            'sav_wisdom_circ': forms.CheckboxInput(attrs={}),
            'sav_wisdom': forms.NumberInput(attrs={'style': sav_value}),
            'sav_charisma_circ': forms.CheckboxInput(attrs={}),
            'sav_charisma': forms.NumberInput(attrs={'style': sav_value}),

            #Skills
            'acrobatics': forms.NumberInput(attrs={'style': skill_value}),
            'animal_handling': forms.NumberInput(attrs={'style': skill_value}),
            'arcana': forms.NumberInput(attrs={'style': skill_value}),
            'athletics': forms.NumberInput(attrs={'style': skill_value}),
            'deception': forms.NumberInput(attrs={'style': skill_value}),
            'history': forms.NumberInput(attrs={'style': skill_value}),
            'insight': forms.NumberInput(attrs={'style': skill_value}),
            'intimidation': forms.NumberInput(attrs={'style': skill_value}),
            'investigation': forms.NumberInput(attrs={'style': skill_value}),
            'medicine': forms.NumberInput(attrs={'style': skill_value}),
            'nature': forms.NumberInput(attrs={'style': skill_value}),
            'perception': forms.NumberInput(attrs={'style': skill_value}),
            'performance': forms.NumberInput(attrs={'style': skill_value}),
            'persuasion': forms.NumberInput(attrs={'style': skill_value}),
            'religion': forms.NumberInput(attrs={'style': skill_value}),
            'sleight_hand': forms.NumberInput(attrs={'style': skill_value}),
            'stealth': forms.NumberInput(attrs={'style': skill_value}),
            'survival': forms.NumberInput(attrs={'style': skill_value}),

            #Armor class, Initiative, Speed
            'armor_class': forms.TextInput(attrs={'style': ac_init_sp}),
            'initiative': forms.NumberInput(attrs={'style': ac_init_sp}),
            'speed': forms.NumberInput(attrs={'style': ac_init_sp}),
            
            #Hitpoint
            'hp_curr': forms.NumberInput(attrs={'style': hitp}),
            'hp_temp': forms.NumberInput(attrs={'style': hitp}),

            #Dice_death
            'hit_dice': forms.TextInput(attrs={'style': dice_dth_left}),
            'dth_succ': forms.NumberInput(attrs={'style': dice_dth_right}),
            'dth_fail': forms.NumberInput(attrs={'style': dice_dth_right}),

            #atk_spell
            'atk_spell_name_1': forms.TextInput(attrs={'style': atk_spell}),
            'atk_spell_bonus_1': forms.NumberInput(attrs={'style': atk_spell}),
            'atk_spell_type_1': forms.TextInput(attrs={'style': atk_spell}),

            'atk_spell_name_2': forms.TextInput(attrs={'style': atk_spell}),
            'atk_spell_bonus_2': forms.NumberInput(attrs={'style': atk_spell}),
            'atk_spell_type_2': forms.TextInput(attrs={'style': atk_spell}),

            'atk_spell_name_3': forms.TextInput(attrs={'style': atk_spell}),
            'atk_spell_bonus_3': forms.NumberInput(attrs={'style': atk_spell}),
            'atk_spell_type_3': forms.TextInput(attrs={'style': atk_spell}),

            'atk_spell_name_4': forms.TextInput(attrs={'style': atk_spell}),
            'atk_spell_bonus_4': forms.NumberInput(attrs={'style': atk_spell}),
            'atk_spell_type_4': forms.TextInput(attrs={'style': atk_spell}),

            'atk_spell_name_5': forms.TextInput(attrs={'style': atk_spell}),
            'atk_spell_bonus_5': forms.NumberInput(attrs={'style': atk_spell}),
            'atk_spell_type_5': forms.TextInput(attrs={'style': atk_spell}),

            #Passive wisdom
            'pass_wisdom': forms.TextInput(attrs={'style': pass_wis}),

            #feat_trait
            'feat_trait': forms.Textarea(attrs={'style': feat_trait}),

        }