from django.db import models
from users.models import User_Extended


class MyInfo(models.Model):
    # link username to username in User_Extended
    username = models.ForeignKey(User_Extended, to_field="username", default=None, on_delete=models.CASCADE)
    # Foreign key to Spells5E name not used as Django expects reference to object, not value https://stackoverflow.com/questions/30017334/django-foreign-key-must-be-an-instance
    class_name = models.CharField(max_length=25, blank = True, null = True)
    level = models.PositiveSmallIntegerField(blank = True, null = True)
    background = models.CharField(max_length=30, blank = True, null = True)
    faction = models.CharField(max_length=30, blank = True, null = True)
    race = models.CharField(max_length=25, blank = True, null = True)
    alignment = models.CharField(max_length=25, blank = True, null = True)
    exp_points = models.PositiveSmallIntegerField(blank = True, null = True)
    dci_number = models.PositiveSmallIntegerField(blank = True, null = True)
    personality_traits = models.CharField(max_length=80, blank = True, null = True)
    ideals = models.CharField(max_length=80, blank = True, null = True)
    bonds = models.CharField(max_length=80, blank = True, null = True)
    flaws = models.CharField(max_length=80, blank = True, null = True)
    background_story = models.CharField(max_length=2500, blank = True, null = True)
    oth_prof_lan = models.CharField(max_length=2000, blank = True, null = True)
    appearance = models.CharField(max_length=250, blank = True, null = True)


