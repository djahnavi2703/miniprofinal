# Generated by Django 5.0.7 on 2024-07-14 02:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_alter_batchmaster_batchid_alter_batchmaster_batchno'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='studentname',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='batchid',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='course',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='examtype',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='papercode',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='sem',
        ),
        migrations.DeleteModel(
            name='StudentMaster',
        ),
        migrations.DeleteModel(
            name='Transaction',
        ),
    ]
