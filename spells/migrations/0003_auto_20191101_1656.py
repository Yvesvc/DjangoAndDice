# Generated by Django 2.2.6 on 2019-11-01 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spells', '0002_spells5e_higher_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='spells5e',
            name='archetype',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='spells5e',
            name='patrons',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]