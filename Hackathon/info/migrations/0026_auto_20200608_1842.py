# Generated by Django 3.0.6 on 2020-06-08 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0025_auto_20200608_1842'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medicalform',
            old_name='BloodGroup',
            new_name='bloodGroup',
        ),
        migrations.RenameField(
            model_name='medicalform',
            old_name='Description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='medicalform',
            old_name='Problem',
            new_name='problem',
        ),
        migrations.RenameField(
            model_name='medicalform',
            old_name='Profile',
            new_name='profile',
        ),
    ]
