from rest_framework import serializers
from posts.models import Post
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    posts_num = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username','weight', 'posts_num']

    def get_posts_num(self, obj):
        return Post.objects.filter(user=obj).count()
