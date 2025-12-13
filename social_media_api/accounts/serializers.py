from rest_framework import serializers
from.models import User


class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True,write_only=True)
    password2 = serializers.CharField(required=True,write_only=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')

    def validate(self,data):
        if User.objects.filter(username=data["username"]).exists():
            raise serializers.ValidationError('Username already exists')
        if User.objects.filter(email=data["email"]).exists():
            raise serializers.ValidationError('Email already exists')
        if data["password"] != data["password2"]:
            raise serializers.ValidationError('Passwords do not match')
        return data
    def create(self,validated_data):
        password2 = validated_data.pop('password2')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'bio', 'followers','profile_picture')
