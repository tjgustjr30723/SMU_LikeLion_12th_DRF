# Generated by Django 5.0.3 on 2024-04-07 13:39

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_height_alter_user_sign_up_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='height',
            field=models.IntegerField(blank=True, default=None, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='user',
            name='old',
            field=models.IntegerField(blank=True, default=None, null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(20)]),
        ),
        migrations.AlterField(
            model_name='user',
            name='sign_up_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 7, 13, 39, 5, 926640, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='weight',
            field=models.IntegerField(blank=True, default=None, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
