from .serializers import ToDoSerializer
from .models import ToDo
from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView, ListAPIView
# Create your views here.

class ListTodoView(ListAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class DetailTodoView(RetrieveAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer