# Generated by Django 5.0.3 on 2024-05-09 03:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0025_post_likes_alter_post_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 9, 3, 41, 1, 43280, tzinfo=datetime.timezone.utc)),
        ),
    ]