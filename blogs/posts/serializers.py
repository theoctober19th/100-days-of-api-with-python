from django.db.models import fields
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    # created_on = serializers.DateTimeField(source='created_at')
    class Meta:
        model = Post
        fields = ('id', 'title', 'body', 'author',)