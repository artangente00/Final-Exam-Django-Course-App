# Generated by Django 3.1.3 on 2021-12-14 00:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0002_auto_20211213_2229'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='lesson',
            new_name='course',
        ),
    ]
