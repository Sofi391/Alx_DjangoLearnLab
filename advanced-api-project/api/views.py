from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer


# ListView: retrieves all books
class BookListView(generics.ListAPIView):
    """
    Returns a list of all Book instances.
    Accessible to anyone (read-only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# DetailView: retrieves a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    """
    Returns a single Book instance by primary key.
    Accessible to anyone (read-only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# CreateView: allows adding a new book
class BookCreateView(generics.CreateAPIView):
    """
    Creates a new Book instance.
    Only authenticated users can create books.
    Custom validation is handled in the serializer.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# UpdateView: modify an existing book
class BookUpdateView(generics.UpdateAPIView):
    """
    Updates an existing Book instance.
    Only authenticated users can update books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# DeleteView: remove a book
class BookDeleteView(generics.DestroyAPIView):
    """
    Deletes an existing Book instance.
    Only authenticated users can delete books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
