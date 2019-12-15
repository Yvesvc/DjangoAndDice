from django.db import models
from users.models import User_Extended

class MyEquipment(models.Model):
    # link username to username in User_Extended
    username = models.ForeignKey(User_Extended, to_field="username", default=None, on_delete=models.CASCADE)
    # (blank = True, null = True) == NULL value allowed
    equipment_text = models.CharField(max_length=5000, blank=True, null=True)