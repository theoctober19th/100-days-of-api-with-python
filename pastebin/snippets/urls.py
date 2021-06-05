
from os import name
from django.conf import urls
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework import renderers
from rest_framework.decorators import renderer_classes
from .views import UserViewSet, SnippetViewSet
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'snippets', SnippetViewSet)

urlpatterns = [
    path('', include(router.urls))
]