# Generated by Django 5.0.3 on 2024-04-08 02:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0009_alter_comment_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 8, 2, 14, 4, 231401, tzinfo=datetime.timezone.utc)),
        ),
    ]
