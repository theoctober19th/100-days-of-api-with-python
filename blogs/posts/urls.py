
from os import name
from django.contrib import admin
from django.urls import path
from .views import PostViewSet, UserViewSet
from rest_framework.routers import SimpleRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

router = SimpleRouter()

router.register("users", UserViewSet, basename="users")
router.register('', PostViewSet, basename="posts")

urlpatterns = router.urls