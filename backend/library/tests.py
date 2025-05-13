from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Book
from django.contrib.auth.models import User

class BookTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.book_data = {'title': 'Test Book', 'author': 'John Doe', 'isbn': '1234567890123'}

    def test_create_book(self):
        response = self.client.post('/api/books/', self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)