from django.contrib import admin
from spells.models import Spells5E, My_Spells, spells_metadata

admin.site.register(Spells5E)
admin.site.register(My_Spells)
admin.site.register(spells_metadata)
