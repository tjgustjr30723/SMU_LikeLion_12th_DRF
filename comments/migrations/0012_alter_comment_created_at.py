# Generated by Django 5.0.3 on 2024-04-08 02:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0011_alter_comment_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 8, 2, 29, 53, 69034, tzinfo=datetime.timezone.utc)),
        ),
    ]
