# Generated by Django 2.0.1 on 2018-02-14 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0004_auto_20180214_1426'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='date',
            new_name='created',
        ),
    ]