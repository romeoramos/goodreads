from django.shortcuts import render
from rest_framework import generics,filters
from .models import Book
from .serializers import BookSerializer
import django_filters.rest_framework
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class ListBook(generics.ListCreateAPIView):

    permission_classes = (IsAuthenticated,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (filters.SearchFilter,django_filters.rest_framework.DjangoFilterBackend,)
    filter_fields = ('name','ISBN','author','category')
    search_fields = ('name','ISBN','description')


class DetailBook(generics.RetrieveUpdateDestroyAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer
