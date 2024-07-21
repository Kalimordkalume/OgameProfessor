# Generated by Django 5.0.6 on 2024-07-14 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empire', '0020_planet_profile_alter_profile_name_building_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technology',
            name='name',
            field=models.CharField(choices=[('1', 'Armor Technology'), ('2', 'Intergalactic Technology'), ('3', 'Plasma Technology')], unique=True),
        ),
    ]