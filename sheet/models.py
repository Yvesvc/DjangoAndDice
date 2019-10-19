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
    animal_handling = models.SmallIntegerField()
    arcana = models.SmallIntegerField()
    athletics = models.SmallIntegerField()
    deception = models.SmallIntegerField()
    history = models.SmallIntegerField()
    insight = models.SmallIntegerField()
    intimidation = models.SmallIntegerField()
    investigation = models.SmallIntegerField()
    medicine = models.SmallIntegerField()
    nature = models.SmallIntegerField()
    perception = models.SmallIntegerField()
    performance = models.SmallIntegerField()
    persuasion = models.SmallIntegerField()
    religion = models.SmallIntegerField()
    sleight_hand = models.SmallIntegerField()
    stealth = models.SmallIntegerField()
    survival = models.SmallIntegerField()
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