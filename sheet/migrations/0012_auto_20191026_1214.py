# Generated by Django 2.2.6 on 2019-10-26 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheet', '0011_auto_20191021_2045'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sheet',
            old_name='atk_spell_bonus',
            new_name='atk_spell_bonus_1',
        ),
        migrations.RenameField(
            model_name='sheet',
            old_name='atk_spell_name',
            new_name='atk_spell_name_1',
        ),
        migrations.RenameField(
            model_name='sheet',
            old_name='atk_spell_type',
            new_name='atk_spell_type_1',
        ),
        migrations.AddField(
            model_name='sheet',
            name='atk_spell_bonus_2',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sheet',
            name='atk_spell_bonus_3',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sheet',
            name='atk_spell_bonus_4',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sheet',
            name='atk_spell_bonus_5',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sheet',
            name='atk_spell_name_2',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='sheet',
            name='atk_spell_name_3',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='sheet',
            name='atk_spell_name_4',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='sheet',
            name='atk_spell_name_5',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='sheet',
            name='atk_spell_type_2',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='sheet',
            name='atk_spell_type_3',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='sheet',
            name='atk_spell_type_4',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='sheet',
            name='atk_spell_type_5',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]