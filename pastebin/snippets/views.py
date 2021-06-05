from django.contrib.auth.models import PermissionManager, User
from django.db.models import query
from snippets.permissions import IsAuthorOrReadOnly
from snippets.serializers import UserSerializer
from django.contrib.auth import get_user, get_user_model
from django.http.response import Http404
from rest_framework.views import APIView
from snippets.serializers import SnippetSerializer
from snippets.models import Snippet
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework import generics
from rest_framework import mixins
from rest_framework import permissions
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

class UserViewSet(ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class SnippetViewSet(ModelViewSet):
    serializer_class = SnippetSerializer
    queryset = Snippet.objects.all()
    PermissionManager = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)