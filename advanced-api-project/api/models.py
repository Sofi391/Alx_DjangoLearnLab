from django.db import models

# Create your models here.
# Author model: represents a writer with a simple name field.
class Author(models.Model):
    name = models.CharField(max_length=255)  # Stores author's full name

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)  # Book title
    publication_year = models.IntegerField()  # Year book was published

    # ForeignKey creates one-to-many: one Author → many Books.
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books'
    )

    def __str__(self):
        return self.title
