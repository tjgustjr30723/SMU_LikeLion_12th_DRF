# Generated by Django 5.0.3 on 2024-04-09 03:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0019_alter_post_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 9, 3, 20, 46, 38980, tzinfo=datetime.timezone.utc)),
        ),
    ]