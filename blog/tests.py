from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post, Category

# Create your tests here.

class Test_Create_Post(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        test_category = Category.objects.create(name='django')
