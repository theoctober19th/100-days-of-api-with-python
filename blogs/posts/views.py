from django.db.models import query
from django.shortcuts import render
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
from rest_framework import permissions
from .permissions import IsAuthorOrReadOnly
# Create your views here.

class PostListView(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated, )
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly, )
    queryset = Post.objects.all()
    serializer_class = PostSerializer