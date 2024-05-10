from django.db import models
from users.models import User
from django.utils import timezone
class Post(models.Model):
    title = models.CharField(max_length=50, null=True)
    content = models.CharField(max_length=200, null = True, blank=True)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    hash_tag = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    view_count = models.PositiveIntegerField(default=0)
    background_music = models.CharField(max_length=100, blank=True)
    attachment_link = models.URLField(max_length=200,blank=True)
    location = models.CharField(max_length=50, blank=True)
    likes = models.ManyToManyField(User, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts',null = True)
