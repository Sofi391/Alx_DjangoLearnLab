# Advanced API Project – Generic Views

## Overview
This project demonstrates the use of Django REST Framework generic views to handle CRUD operations for the Book model.

## Views Summary
- **BookListView** — Lists all books (public access)
- **BookDetailView** — Retrieves a book by ID (public access)
- **BookCreateView** — Creates a book (authenticated users only)
- **BookUpdateView** — Updates a book (authenticated users only)
- **BookDeleteView** — Deletes a book (authenticated users only)

## URL Endpoints
- `/api/books/`
- `/api/books/<pk>/`
- `/api/books/create/`
- `/api/books/<pk>/update/`
- `/api/books/<pk>/delete/`

## Notes
- Permissions are enforced using DRF’s permission classes.
- Validation is handled inside `BookSerializer`.
- Views may be extended using `perform_create`, `perform_update`, or custom filters.


## Filtering, Searching, and Ordering

This project uses Django REST Framework's advanced query features on the BookListView.

### Filtering
You can filter books using:
- title
- author (FK)
- publication_year

**Examples:**
- `/api/books/?title=Harry Potter`
- `/api/books/?publication_year=2020`
- `/api/books/?author=3`

### Searching
Search is enabled on:
- title
- author name

**Examples:**
- `/api/books/?search=potter`
- `/api/books/?search=rowling`

### Ordering
Books can be ordered by:
- title
- publication_year

**Examples:**
- `/api/books/?ordering=title`
- `/api/books/?ordering=-publication_year`
