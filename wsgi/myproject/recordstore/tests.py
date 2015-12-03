from django.test import TestCase, RequestFactory, Client
from django.contrib.auth.models import User as Modeluser
import json

from .models import *
from .views import *
from .search import *

class CollectionTest(TestCase):
    """
    fixtures = ['test_data.json',] 

    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

        success = self.client.login(username='jlagrou2', password='RunCat941')
        self.assertTrue(success)

    def test_add_to_collection(self):
        album = Album.objects.get(pk=1)
        pressing = album.pressing_set.all()[0]
        post_data = {
            'album_id' : album.id,
            'pressing_id' : pressing.id,
        }
        response = self.client.post('/recordstore/collection/add', post_data)
        self.assertEqual(response.status_code, 200)

        decoder = json.JSONDecoder()
        response_json = decoder.decode(response.content)

        self.assertTrue(response_json['success'])
    """
    pass
