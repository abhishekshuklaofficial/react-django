# Generated by Django 2.2.13 on 2022-09-02 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0002_auto_20220902_0659'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='imagess',
        ),
    ]