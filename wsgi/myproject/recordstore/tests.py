from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User as Modeluser

from .models import *
from .views import *

# Create your tests here.

class CollectionTest(TestCase):

    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

        model_user = ModelUser.objects.create_user(
            username='jacob', 
            email='jacob@fakedomain.com', 
            password='top_secret')
        self.user = User.objects.create(user=model_user)

    def test_add_to_collection(self):
        request = self.factory.get('/recordstore/collection/add')


    def test_working(self):
        self.assertEqual(200, 200)
