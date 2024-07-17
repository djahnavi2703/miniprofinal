# Generated by Django 5.0.7 on 2024-07-13 16:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_alter_batchmaster_batchid_alter_batchmaster_batchno'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentmaster',
            old_name='batchno',
            new_name='batchid',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='batchno',
            new_name='batchid',
        ),
        migrations.AlterField(
            model_name='batchmaster',
            name='batchid',
            field=models.CharField(max_length=2, validators=[django.core.validators.RegexValidator(message='Enter only integer.', regex='^[0-9]+$')]),
        ),
        migrations.AlterField(
            model_name='batchmaster',
            name='batchno',
            field=models.CharField(choices=[(' ', 'Select_Batch'), ('2020-2022', '2020-2022'), ('2021-2023', '2021-2023'), ('2022-2024', '2022-2024'), ('2023-2025', '2023-2025'), ('2024-2025', '2024-2025'), ('2025-2027', '2025-2027'), ('2026-2028', '2026-2028'), ('2027-2029', '2027-2029'), ('2028-2030', '2028-2030')], default=' ', max_length=10),
        ),
    ]