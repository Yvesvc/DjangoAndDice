# Generated by Django 2.2.6 on 2019-11-07 18:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('spells', '0010_auto_20191107_1935'),
    ]

    operations = [
        migrations.CreateModel(
            name='spells_metadata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scability', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('ssdc', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('sabonus', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('lvl1_total', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('lvl1_left', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('lvl2_total', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('lvl2_left', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('lvl3_total', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('lvl3_left', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('lvl4_total', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('lvl4_left', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('lvl5_total', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('lvl5_left', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('lvl6_total', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('lvl6_left', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('lvl7_total', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('lvl7_left', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('lvl8_total', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('lvl8_left', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('lvl9_total', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('lvl9_left', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('username', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
        ),
    ]