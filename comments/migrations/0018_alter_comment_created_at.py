# Generated by Django 5.0.3 on 2024-05-09 03:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0017_alter_comment_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 9, 3, 25, 47, 704912, tzinfo=datetime.timezone.utc)),
        ),
    ]