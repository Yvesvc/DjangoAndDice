# Generated by Django 2.2.6 on 2019-11-01 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spells', '0003_auto_20191101_1656'),
    ]

    operations = [
        migrations.AddField(
            model_name='spells5e',
            name='domains',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
