from django.contrib.auth.models import User
from django.db.models import query
from django.shortcuts import render
from django.views import generic
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer, UserSerializer
from rest_framework import permissions
from .permissions import IsAuthorOrReadOnly
from django.contrib.auth import get_user, get_user_model
from rest_framework.viewsets import ModelViewSet
# Create your views here.

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly, )

class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer