from rest_framework import serializers
from posts.models import Post
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    posts_num = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username','password','email','weight', 'posts_num']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    def get_posts_num(self, obj):
        return Post.objects.filter(user=obj).count()
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
