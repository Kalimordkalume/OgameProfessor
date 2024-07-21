# Generated by Django 5.0.6 on 2024-07-09 18:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountTechnologiesDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('energy_technology_level', models.PositiveSmallIntegerField(default=0)),
                ('laser_technology_level', models.PositiveSmallIntegerField(default=0)),
                ('ion_technology_level', models.PositiveSmallIntegerField(default=0)),
                ('hyperspace_technology_level', models.PositiveSmallIntegerField(default=0)),
                ('plasma_technology_level', models.PositiveSmallIntegerField(default=0)),
                ('combustion_drive_level', models.PositiveSmallIntegerField(default=0)),
                ('impulsive_drive_level', models.PositiveSmallIntegerField(default=0)),
                ('hyperspace_drive_level', models.PositiveSmallIntegerField(default=0)),
                ('espionage_technology_level', models.PositiveSmallIntegerField(default=0)),
                ('computer_technology_level', models.PositiveSmallIntegerField(default=0)),
                ('astrophysics_level', models.PositiveSmallIntegerField(default=0)),
                ('intergalactic_research_network_level', models.PositiveSmallIntegerField(default=0)),
                ('weapons_technology_level', models.PositiveSmallIntegerField(default=0)),
                ('shielding_technology_level', models.PositiveSmallIntegerField(default=0)),
                ('armour_technology_level', models.PositiveSmallIntegerField(default=0)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AccountUserSettingDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('universe_economy', models.PositiveSmallIntegerField(default=1)),
                ('account_class', models.CharField(choices=[('G', 'General'), ('D', 'Discoverer'), ('M', 'Merchant')], max_length=1)),
                ('user_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Account User Setting',
                'verbose_name_plural': 'Account Users Settings',
                'db_table': 'Account Settings Table',
            },
        ),
        migrations.CreateModel(
            name='PlanetDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('planet_name', models.CharField(blank=True, max_length=50, verbose_name='Planet Name')),
                ('planet_temperature', models.SmallIntegerField(default=0, verbose_name='Cuca')),
                ('planet_galaxy', models.PositiveSmallIntegerField(default=1, verbose_name='Galaxy')),
                ('planet_system', models.PositiveSmallIntegerField(default=1, verbose_name='Solar System')),
                ('planet_position', models.PositiveSmallIntegerField(default=1, verbose_name='Planet Position')),
                ('account_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empire.accountusersettingdb')),
            ],
            options={
                'verbose_name': 'Planet',
                'verbose_name_plural': 'Planets',
                'db_table': 'Planets Table',
            },
        ),
    ]