# Generated by Django 2.1a1 on 2018-08-31 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20180831_1438'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermodel',
            old_name='name',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='usermodel',
            old_name='password',
            new_name='lastname',
        ),
    ]