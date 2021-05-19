from django.db import models
from django.db.models.base import Model

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=64)
    isbn = models.CharField(max_length=16)
    author = models.CharField(max_length=64)

    def __str__(self):
        return self.title