# Generated by Django 3.1.1 on 2020-10-08 08:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20201008_0840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='date_of_birth',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 10, 8, 8, 44, 37, 510474)),
        ),
    ]
