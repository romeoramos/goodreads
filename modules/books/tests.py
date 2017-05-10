from django.test import TestCase
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book
from modules.authors.models import Author
import json

# Create your tests here.
class BookListTest(APITestCase):

    def setUp(self):
        self.author = Author()
        self.author.name = "Un autor"
        self.author.lastname = "Apellidos"
        self.author.nationality = "Mexicana"
        self.author.bio = ""
        self.author.sex = "M"
        self.author.age = 20
        self.author.category = "ROM"
        self.author.save()
        self.book = { "name":"Un libro",
        "ISBN":"123456789",
        "author":self.author.id,
        "description":"XXXXXX",
        "rating":0.00
        }
        self.url = reverse('list-books')

    def test_list_books(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_create_books(self):
        response = self.client.post(self.url,self.book,format='json')
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

class BookDetailTest(APITestCase):

    def setUp(self):
        self.author = Author()
        self.author.name = "Un autor"
        self.author.lastname = "Apellidos"
        self.author.nationality = "Mexicana"
        self.author.bio = ""
        self.author.sex = "M"
        self.author.age = 20
        self.author.category = "ROM"
        self.author.save()

        self.book = Book(name="un libro",
        author=self.author,
        ISBN="1234567890",
        description="",
        rating=0.00)
        self.book.save()
        self.url = reverse('details-books',args=[self.book.id])

    def test_retrieve_book(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_update_book(self): #'id','name','description','ISBN','book_comments','author'
        self.data = { "name":"Un libro",
        "ISBN":"123456789",
        "author":self.author.id,
        "description":"XXXXXX"
        }
        response = self.client.put(self.url,self.data,format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        #self.assertEqual(response.data,self.data)

    def test_destroy_book(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)
