from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ["id", "created_datetime"]


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["username", "title", "content"]
        extra_kwargs = {
            "id": {"read_only": True},
            "created_datetime": {"read_only": True},
            "username": {"required": True},
            "title": {"required": True},
            "content": {"required": True},
        }
        read_only_fields = ["created_datetime"]


class PostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["title", "content"]
        extra_kwargs = {
            "title": {"required": True},
            "content": {"required": True},
        }
        read_only_fields = ["created_datetime"]
