from django.test import TestCase

from django.test.client import Client
c = Client()
response = c.post('/login/', {'username': 'john', 'password': 'smith'})
response.status_code

response = c.get('/customer/details/')
response.content
'<!DOCTYPE html...'

c = Client()
c.login(username='fred', password='secret')
# --------------------------------------------
from django.utils import unittest
from django.test.client import Client

class SimpleTest(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_details(self):
        # Issue a GET request.
        response = self.client.get('/customer/details/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that the rendered context contains 5 customers.
        self.assertEqual(len(response.context['customers']), 5)

# -------------------------------------------------

        from django.utils import unittest
        from django.test.client import Client

        class SimpleTest(unittest.TestCase):
            def test_details(self):
                client = Client()
                response = client.get('/customer/details/')
                self.assertEqual(response.status_code, 200)

            def test_index(self):
                client = Client()
                response = client.get('/customer/index/')
                self.assertEqual(response.status_code, 200)