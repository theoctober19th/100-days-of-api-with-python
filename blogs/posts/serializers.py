from django.db.models import fields
from rest_framework import serializers
from .models import Post
from django.contrib.auth import get_user_model

class PostSerializer(serializers.ModelSerializer):
    # created_on = serializers.DateTimeField(source='created_at')
    class Meta:
        model = Post
        fields = ('id', 'title', 'body', 'author',)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username')