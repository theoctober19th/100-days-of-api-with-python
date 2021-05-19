from re import I
from django.contrib import admin
from django.urls import path, include
from .views import BooksApiListView

urlpatterns = [
    path('books/', BooksApiListView.as_view(), name='api_list_books')
]
