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
