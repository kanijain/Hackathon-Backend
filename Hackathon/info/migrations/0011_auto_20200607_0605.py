# Generated by Django 3.0.6 on 2020-06-07 06:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0007_auto_20200604_2026'),
        ('info', '0010_auto_20200607_0601'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='FoodChoice',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='food.Category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='LactoseIntolerance',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
