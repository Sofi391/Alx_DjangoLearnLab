from rest_framework import serializers
from .models import Post,Comment
from django.contrib.auth import get_user_model

class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Post
        fields = ('id','title','content','author','created_at','updated_at')


class CommentSerializer(serializers.ModelSerializer):
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Comment
        fields = "__all__"


User = get_user_model()

class FollowSerializer(serializers.ModelSerializer):
    target_user_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = User
        fields = ('target_user_id',)

    def validate_target_user_id(self, value):
        user = self.context['request'].user
        if user.id == value:
            raise serializers.ValidationError("You cannot follow/unfollow yourself.")
        if not User.objects.filter(id=value).exists():
            raise serializers.ValidationError("User does not exist.")
        return value
