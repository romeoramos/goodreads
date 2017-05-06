from rest_framework import serializers
from .models import Author
from modules.books.serializers import BookNewSerializer

class AuthorSerializer(serializers.ModelSerializer):
    author_books = BookNewSerializer(read_only=True,many=True)
    class Meta:
        model = Author
        fields = ("id","name","lastname","nationality","bio","author_books")
