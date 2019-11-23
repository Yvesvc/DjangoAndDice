from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='spells_index'),
    path('addlevel', views.addlevel, name='add_level'),
    path('deletelevel', views.deletelevel, name='delete_level')
]
