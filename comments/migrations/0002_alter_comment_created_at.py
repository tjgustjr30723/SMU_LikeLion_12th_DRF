# Generated by Django 5.0.3 on 2024-04-07 14:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 7, 14, 45, 21, 520079, tzinfo=datetime.timezone.utc)),
        ),
    ]
