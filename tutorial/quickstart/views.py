from django.contrib.auth.models import Group

from rest_framework import permissions
from quickstart.serializers import GroupSerializer, UserSerializer
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
# Create your views here.

class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, ]
    queryset = get_user_model().objects.all().order_by('-date_joined')

class GroupViewSet(ModelViewSet):
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated, ]
    queryset = Group.objects.all()