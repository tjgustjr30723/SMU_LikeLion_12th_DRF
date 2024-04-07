from django.db import models
from users.models import User
from posts.models import Post
from comments.models import Comment

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes', null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes', null=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='likes', null=True)
