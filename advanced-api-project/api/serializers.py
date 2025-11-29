from rest_framework import serializers
from .models import Author, Book
from datetime import datetime


# Serializer for Book model.
# Includes custom validation to prevent publication_year from being in the future.
class BookSerializer(serializers.ModelSerializer):

    def validate_publication_year(self, value):
        # Ensures publication year is not greater than the current year.
        if value > datetime.now().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

    class Meta:
        model = Book
        fields = '__all__'  # Serializes all fields of the Book model


class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']  # Author name + nested list of books
