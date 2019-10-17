# users/admin.py
from django.contrib import admin
from .models import User_Extended

admin.site.register(User_Extended)