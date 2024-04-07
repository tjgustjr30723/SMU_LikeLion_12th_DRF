# Generated by Django 5.0.3 on 2024-04-07 13:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('comments', '0001_initial'),
        ('posts', '0003_post_attachment_link_post_background_music_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='comments.comment')),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='posts.post')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='likes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
