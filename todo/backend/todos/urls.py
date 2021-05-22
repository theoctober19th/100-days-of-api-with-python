from .views import DetailTodoView, ListTodoView
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', ListTodoView.as_view(), name='list'),
    path('<int:pk>', DetailTodoView.as_view(), name='detail')
]
