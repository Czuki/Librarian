from django.test import TestCase, Client
from django.contrib.auth.models import User
from ..models import Author, Book, Profile, Review
from django.urls import reverse


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()

        self.home_url = reverse('index')

        self.add_book_url = reverse('add-book')
        self.add_author_url = reverse('add-author')

        self.list_books_url = reverse('list-books')
        self.list_authors_url = reverse('list-authors')

        self.book_details_url = reverse('details-book', args=[1])
        self.author_details_url = reverse('details-author', args=[1])

        self.profile_url = reverse('profile')
        self.reviews = reverse('reviews')

        self.signup = reverse('signup')

        self.author = Author.objects.create(author='John Wick')

        self.book = Book.objects.create(name='Titles', isbn='1234567890124', author=self.author)

        self.user = User.objects.create_user(username='Name', password='password')

    def test_homepage_GET(self):
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)

    def test_add_book_url_GET(self):
        response = self.client.get(self.add_book_url)
        self.assertEqual(response.status_code, 200)

    def test_add_author_url_GET(self):
        response = self.client.get(self.add_author_url)
        self.assertEqual(response.status_code, 200)

    def test_list_books_url_GET(self):
        response = self.client.get(self.list_books_url)
        self.assertEqual(response.status_code, 200)

    def test_list_authors_url_GET(self):
        response = self.client.get(self.list_authors_url)
        self.assertEqual(response.status_code, 200)

    def test_book_details_url_GET(self):
        response = self.client.get(self.book_details_url)
        self.assertEqual(response.status_code, 200)

    def test_author_details_url_GET(self):
        response = self.client.get(self.author_details_url)
        self.assertEqual(response.status_code, 200)

    def test_profile_url_GET(self):
        self.client.login(username='Name', password='password')
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, 200)

    def test_signup_user_created_POST(self):
        response = self.client.post(self.signup,
                                    {'username': 'User12345',
                                     'password1': 'Passwords221',
                                     'password2': 'Passwords221'})

        self.assertEqual(response.status_code, 302)
        self.client.logout()
        self.client.login(username='User12345', password='Passwords221')
        response2 = self.client.get(self.profile_url)
        self.assertEqual(response2.status_code, 200)

    def test_add_book_is_created_POST(self):
        response = self.client.post(self.add_book_url,
                                    {'title': 'NEW TITLE',
                                     'author': self.author.id,
                                     'isbn': '1231232121111'})
        self.assertEqual(response.status_code, 302)
        added_book = Book.objects.get(name='NEW TITLE')
        self.assertEqual(added_book.isbn, '1231232121111')

    def test_add_author_is_created_POST(self):
        response = self.client.post(self.add_author_url,
                                    {'first_name': 'FIRSTNAME',
                                     'last_name': 'LASTNAME'})
        added_author = Author.objects.get(author='FIRSTNAME LASTNAME')
        self.assertEqual(added_author.author, 'FIRSTNAME LASTNAME')
