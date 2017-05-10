from rest_framework import serializers
from .models import Book, Comments
from modules.users.serializers import UserSerializer
#from modules.authors.serializers import AuthorSerializer

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Comments
        fields = ('user','comment')


class BookSerializer(serializers.ModelSerializer):
    #author_name = serializers.CharField(source="author.name")
    #author_lastname = serializers.CharField(source="author.lastname")
    #author = AuthorSerializer(read_only=True)
    book_comments = CommentSerializer(read_only=True,many=True)
    class Meta:
        model = Book
        #exclude = ("rating",)
        fields = ('id','name','description','ISBN','book_comments','author')

class BookNewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ("__all__")
