from django.db import models
from django.contrib.auth.models import User
from users.models import User_Extended

class Sheet(models.Model):
    #link username to username in User_Extended
    username = models.ForeignKey(User_Extended, to_field = "username", default = None,on_delete=models.CASCADE)
    level = models.PositiveSmallIntegerField(default = 0)
    strength = models.PositiveSmallIntegerField()
    strength_mod = models.PositiveSmallIntegerField()
    dexterity = models.PositiveSmallIntegerField()
    dexterity_mod = models.PositiveSmallIntegerField()
    constitution = models.PositiveSmallIntegerField()
    constitution_mod = models.PositiveSmallIntegerField()
    intelligence = models.PositiveSmallIntegerField()
    intelligence_mod = models.PositiveSmallIntegerField()
    wisdom = models.PositiveSmallIntegerField()
    wisdom_mod = models.PositiveSmallIntegerField()
    charisma = models.PositiveSmallIntegerField()
    charisma_mod = models.PositiveSmallIntegerField()
    inspiration = models.PositiveSmallIntegerField()
    proficiency = models.PositiveSmallIntegerField()
    sav_strength = models.SmallIntegerField()
    sav_dexterity = models.SmallIntegerField()
    sav_constitution = models.SmallIntegerField()
    sav_intelligence = models.SmallIntegerField()
    sav_wisdom = models.SmallIntegerField()
    sav_charisma = models.SmallIntegerField()
    acrobatics = models.SmallIntegerField()
    acrobatics_circ= models.BooleanField()
    animal_handling = models.SmallIntegerField()
    animal_handling_circ= models.BooleanField()
    arcana = models.SmallIntegerField()
    arcana_circ= models.BooleanField()
    athletics = models.SmallIntegerField()
    athletics_circ= models.BooleanField()
    deception = models.SmallIntegerField()
    deception_circ= models.BooleanField()
    history = models.SmallIntegerField()
    history_circ= models.BooleanField()
    insight = models.SmallIntegerField()
    insight_circ= models.BooleanField()
    intimidation = models.SmallIntegerField()
    intimidation_circ= models.BooleanField()
    investigation = models.SmallIntegerField()
    investigation_circ= models.BooleanField()
    medicine = models.SmallIntegerField()
    models_circ= models.BooleanField()
    nature = models.SmallIntegerField()
    nature_circ= models.BooleanField()
    perception = models.SmallIntegerField()
    perception_circ= models.BooleanField()
    performance = models.SmallIntegerField()
    performance_circ= models.BooleanField()
    persuasion = models.SmallIntegerField()
    persuasion_circ= models.BooleanField()
    religion = models.SmallIntegerField()
    religion_circ= models.BooleanField()
    sleight_hand = models.SmallIntegerField()
    sleigth_hand_circ= models.BooleanField()
    stealth = models.SmallIntegerField()
    stealth_circ= models.BooleanField()
    survival = models.SmallIntegerField()
    survival_circ= models.BooleanField()
    armor_class = models.CharField(max_length = 10)
    initiative = models.SmallIntegerField()
    speed = models.PositiveSmallIntegerField()
    hp_curr = models.PositiveSmallIntegerField()
    hp_temp = models.PositiveSmallIntegerField()
    hit_dice = models.CharField(max_length=10)
    dth_succ = models.PositiveSmallIntegerField()
    dth_fail = models.PositiveSmallIntegerField()
    atk_spell_name = models.CharField(max_length=20)
    atk_spell_bonus = models.PositiveSmallIntegerField()
    atk_spell_type = models.CharField(max_length=10)
    pass_wisdom = models.PositiveSmallIntegerField()
    oth_prof_lang = models.CharField(max_length=1000)
    feat_trait = models.CharField(max_length=2000)