
from django.contrib import admin
from django.urls import path
from .views import PostListView, PostDetailView

urlpatterns = [
    path('posts/', PostListView.as_view(), name='post_lists'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail')
]
