from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User
# Create your tests here.
class TestPosts(TestCase):

    @classmethod
    def setUpClass(self):
        super().setUpClass()
        test_user = User.objects.create(username="test", password="test")
        Post.objects.create(
            title='testtitle',
            body='testbody',
            author=test_user,
        )

    def test_post(self):
        post = Post.objects.all().first()
        self.assertEqual(post.title, 'testtitle')
        self.assertEqual(post.body, 'testbody')
        self.assertEqual(post.author.username, 'test')
