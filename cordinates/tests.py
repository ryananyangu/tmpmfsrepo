import json
from django.test import TestCase, Client
from django.contrib.auth.models import User

# Create your tests here.
class CordinatesTestCase(TestCase):
    c = Client()
    def setUp(self) -> None:
        super().setUp()
        user = User()
        user.username = 'test_user'
        user.password = 'password123'
        user.save()
        CordinatesTestCase.c.force_login(user,backend=None)
        

    def test_post_api(self):
        # Testing happy path
        response  = CordinatesTestCase.c.post('/cordinates/check/',json.dumps("(1,2),(3,4),(14,2)"),content_type='application/json')
        self.assertEqual(response.status_code,201)
        # Testing same cordinates
        response  = CordinatesTestCase.c.post('/cordinates/check/',json.dumps("(1,2),(1,2),(1,2)"),content_type='application/json')
        self.assertEqual(response.status_code,201)
        # Testing malformed request
        response  = CordinatesTestCase.c.post('/cordinates/check/',json.dumps("(1,2),(3,4),(14,b)"),content_type='application/json')
        self.assertEqual(response.status_code,400)
        # Testing request with different datatypes
        response  = CordinatesTestCase.c.post('/cordinates/check/',json.dumps("('a','b'),('c','d'),('e','f')"),content_type='application/json')
        self.assertEqual(response.status_code,400)

        response  = CordinatesTestCase.c.post('/cordinates/check/',json.dumps("The quick brown fox"),content_type='application/json')
        self.assertEqual(response.status_code,400)