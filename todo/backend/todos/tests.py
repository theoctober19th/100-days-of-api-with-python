from django.test import TestCase
from .models import ToDo

# Create your tests here.
class TodoTests(TestCase):

    def setUp(self):
        ToDo.objects.create(title="ANSI", description="Everest")

    def test_title(self):
        todo = ToDo.objects.all().first()
        self.assertEqual(todo.title, "ANSI")

    def test_description(self):
        todo = ToDo.objects.all().first()
        self.assertEqual(todo.description, "Everest")