# Generated by Django 3.0.6 on 2020-06-08 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0022_auto_20200607_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailydiet',
            name='Amount',
            field=models.DecimalField(decimal_places=1, max_digits=10),
        ),
    ]
