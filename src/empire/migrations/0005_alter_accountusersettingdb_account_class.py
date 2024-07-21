# Generated by Django 5.0.6 on 2024-07-09 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empire', '0004_alter_accountusersettingdb_account_class'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountusersettingdb',
            name='account_class',
            field=models.CharField(blank=True, choices=[('G', 'General'), ('D', 'Discoverer'), ('M', 'Merchant')], max_length=1, null=True),
        ),
    ]
