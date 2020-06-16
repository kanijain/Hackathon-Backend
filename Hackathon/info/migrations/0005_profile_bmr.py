# Generated by Django 3.0.2 on 2020-05-18 10:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0004_profile_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='BMR',
            field=models.FloatField(default=677, validators=[django.core.validators.MinValueValidator(0.9), django.core.validators.MaxValueValidator(10000)]),
            preserve_default=False,
        ),
    ]
