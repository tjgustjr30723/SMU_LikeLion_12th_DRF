# Generated by Django 5.0.3 on 2024-04-07 13:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_gender_user_height_user_old_user_profile_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='sign_up_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 7, 13, 22, 34, 631494, tzinfo=datetime.timezone.utc)),
        ),
    ]
