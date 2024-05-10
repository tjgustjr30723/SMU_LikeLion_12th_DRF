from rest_framework import serializers
from posts.models import Post
from users.serializers import UserSerializer

class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(required = False)
    likes_num = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = "__all__"

    def get_likes_num(self, obj):
        return obj.likes.count()