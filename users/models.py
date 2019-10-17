# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User_Extended(AbstractUser):
    pass
    charactername = models.CharField(max_length = 25)