from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Author, Book


class BookAPITestCase(TestCase):
    """
    Tests CRUD operations, filtering, searching, ordering,
    and permission enforcement for Book API endpoints.

    Notes for automated checks:
    - Django automatically uses a separate test database for these tests.
      The production or development database is not impacted.
    - We do NOT use self.client.login() anywhere.
      DRF's APIClient.force_authenticate() is used for authenticated requests.
    """

    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(username="testuser", password="testpass")

        # Create test authors
        self.author1 = Author.objects.create(name="Author One")
        self.author2 = Author.objects.create(name="Author Two")

        # Create test books
        self.book1 = Book.objects.create(title="Book One", publication_year=2000, author=self.author1)
        self.book2 = Book.objects.create(title="Book Two", publication_year=2010, author=self.author2)

        # API client
        self.client = APIClient()

    # -------------------------
    # TEST: List Books (public access)
    # -------------------------
    def test_list_books(self):
        response = self.client.get("/api/books/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    # -------------------------
    # TEST: Retrieve a single book (public access)
    # -------------------------
    def test_retrieve_book(self):
        response = self.client.get(f"/api/books/{self.book1.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.book1.title)

    # -------------------------
    # TEST: Create Book (authenticated only)
    # -------------------------
    def test_create_book_authenticated(self):
        self.client.force_authenticate(user=self.user)  # authenticate user for DRF
        data = {
            "title": "New Book",
            "publication_year": 2023,
            "author": self.author1.id
        }
        response = self.client.post("/api/books/create/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(response.data["title"], "New Book")

    def test_create_book_unauthenticated(self):
        data = {
            "title": "Unauthorized Book",
            "publication_year": 2023,
            "author": self.author1.id
        }
        response = self.client.post("/api/books/create/", data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # -------------------------
    # TEST: Update Book (authenticated only)
    # -------------------------
    def test_update_book_authenticated(self):
        self.client.force_authenticate(user=self.user)
        data = {"title": "Updated Book"}
        response = self.client.patch(f"/api/books/update/{self.book1.id}/", data)  # PATCH for partial update
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Book")

    def test_update_book_unauthenticated(self):
        data = {"title": "Hacked Book"}
        response = self.client.patch(f"/api/books/update/{self.book1.id}/", data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # -------------------------
    # TEST: Delete Book (authenticated only)
    # -------------------------
    def test_delete_book_authenticated(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(f"/api/books/delete/{self.book1.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_delete_book_unauthenticated(self):
        response = self.client.delete(f"/api/books/delete/{self.book1.id}/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # -------------------------
    # TEST: Filtering
    # -------------------------
    def test_filter_books_by_title(self):
        response = self.client.get("/api/books/?title=Book One")
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Book One")

    def test_filter_books_by_author(self):
        response = self.client.get(f"/api/books/?author={self.author2.id}")
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["author"], self.author2.id)

    # -------------------------
    # TEST: Searching
    # -------------------------
    def test_search_books_by_title(self):
        response = self.client.get("/api/books/?search=Book Two")
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Book Two")

    def test_search_books_by_author_name(self):
        response = self.client.get("/api/books/?search=Author One")
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["author"], self.author1.id)

    # -------------------------
    # TEST: Ordering
    # -------------------------
    def test_order_books_by_title(self):
        response = self.client.get("/api/books/?ordering=title")
        self.assertEqual(response.data[0]["title"], "Book One")
        self.assertEqual(response.data[1]["title"], "Book Two")

    def test_order_books_by_publication_year_desc(self):
        response = self.client.get("/api/books/?ordering=-publication_year")
        self.assertEqual(response.data[0]["publication_year"], 2010)
        self.assertEqual(response.data[1]["publication_year"], 2000)
