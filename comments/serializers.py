from rest_framework import serializers
from comments.models import Comment
from users.serializers import UserSerializer
from posts.serializers import PostSerializer

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    post = PostSerializer()
    class Meta:
        model = Comment
        fields = "__all__"