# Generated by Django 5.0.3 on 2024-04-08 02:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0015_alter_post_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 8, 2, 11, 17, 732079, tzinfo=datetime.timezone.utc)),
        ),
    ]
