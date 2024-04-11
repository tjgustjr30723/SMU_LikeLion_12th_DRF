from rest_framework import serializers
from likes.models import Like
from users.serializers import UserSerializer
from posts.serializers import PostSerializer
from comments.serializers import CommentSerializer

class LikeSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    post = PostSerializer()
    comment = CommentSerializer()
    class Meta:
        model = Like
        fields = "__all__"