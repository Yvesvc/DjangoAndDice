from django.db import models


class Spells5E(models.Model):
    name = models.CharField(max_length=100, blank = True, null = True)
    desc =models.CharField(max_length=5000, blank = True, null = True)
    higher_level = models.CharField(max_length=1000, blank = True, null = True)
    page = models.CharField(max_length=20, blank = True, null = True)
    range = models.CharField(max_length=20, blank = True, null = True)
    components = models.CharField(max_length=100, blank = True, null = True)
    material = models.CharField(max_length=100, blank = True, null = True)
    ritual =models.CharField(max_length=20, blank = True, null = True)
    duration = models.CharField(max_length=20, blank = True, null = True)
    concentration = models.CharField(max_length=20, blank = True, null = True)
    casting_time = models.CharField(max_length=20, blank = True, null = True)
    level = models.CharField(max_length=20, blank = True, null = True)
    school = models.CharField(max_length=20, blank = True, null = True)
    char_class = models.CharField(max_length=100, blank = True, null = True)
    archetype = models.CharField(max_length=50, blank=True, null=True)
    domains = models.CharField(max_length=20, blank=True, null=True)
    patrons = models.CharField(max_length=20, blank=True, null=True)
    oaths = models.CharField(max_length=20, blank=True, null=True)
    circles = models.CharField(max_length=20, blank=True, null=True)