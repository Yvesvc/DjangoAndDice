from django.db import models
from users.models import User_Extended

class Spells5E(models.Model):
    name = models.CharField(max_length=50, blank = True, null = True, unique = True)
    desc = models.CharField(max_length=4500, blank = True, null = True)
    higher_level = models.CharField(max_length=750, blank = True, null = True)
    page = models.CharField(max_length=25, blank = True, null = True)
    range = models.CharField(max_length=50, blank = True, null = True)
    components = models.CharField(max_length=15, blank = True, null = True)
    material = models.CharField(max_length=1000, blank = True, null = True)
    ritual =models.CharField(max_length=10, blank = True, null = True)
    duration = models.CharField(max_length=50, blank = True, null = True)
    concentration = models.CharField(max_length=10, blank = True, null = True)
    casting_time = models.CharField(max_length=50, blank = True, null = True)
    level = models.CharField(max_length=50, blank = True, null = True)
    school = models.CharField(max_length=50, blank = True, null = True)
    char_class = models.CharField(max_length=100, blank = True, null = True)
    archetype = models.CharField(max_length=100, blank=True, null=True)
    domains = models.CharField(max_length=50, blank=True, null=True)
    patrons = models.CharField(max_length=50, blank=True, null=True)
    oaths = models.CharField(max_length=50, blank=True, null=True)
    circles = models.CharField(max_length=50, blank=True, null=True)


class My_Spells(models.Model):
    # link username to username in User_Extended
    username = models.ForeignKey(User_Extended, to_field="username", default=None, on_delete=models.CASCADE)
    # Foreign key to Spells5E name not used as Django expects reference to object, not value https://stackoverflow.com/questions/30017334/django-foreign-key-must-be-an-instance
    name = models.CharField(max_length=50, blank=True, null=True)

class spells_metadata(models.Model):
    # link username to username in User_Extended
    username = models.ForeignKey(User_Extended, to_field="username", default=None, on_delete=models.CASCADE)
    scability = models.PositiveSmallIntegerField(blank = True, null = True)
    ssdc = models.PositiveSmallIntegerField(blank = True, null = True)
    sabonus = models.PositiveSmallIntegerField(blank = True, null = True)
    lvl1_total = models.PositiveSmallIntegerField(blank = True, null = True)
    lvl1_left = models.PositiveSmallIntegerField(blank = True, null = True)
    lvl2_total = models.PositiveSmallIntegerField(blank = True, null = True)
    lvl2_left = models.PositiveSmallIntegerField(blank = True, null = True)
    lvl3_total = models.PositiveSmallIntegerField(blank = True, null = True)
    lvl3_left = models.PositiveSmallIntegerField(blank = True, null = True)
    lvl4_total = models.PositiveSmallIntegerField(blank = True, null = True)
    lvl4_left = models.PositiveSmallIntegerField(blank = True, null = True)
    lvl5_total = models.PositiveSmallIntegerField(blank = True, null = True)
    lvl5_left = models.PositiveSmallIntegerField(blank = True, null = True)
    lvl6_total = models.PositiveSmallIntegerField(blank = True, null = True)
    lvl6_left = models.PositiveSmallIntegerField(blank = True, null = True)
    lvl7_total = models.PositiveSmallIntegerField(blank = True, null = True)
    lvl7_left = models.PositiveSmallIntegerField(blank = True, null = True)
    lvl8_total = models.PositiveSmallIntegerField(blank = True, null = True)
    lvl8_left = models.PositiveSmallIntegerField(blank = True, null = True)
    lvl9_total = models.PositiveSmallIntegerField(blank = True, null = True)
    lvl9_left = models.PositiveSmallIntegerField(blank = True, null = True)