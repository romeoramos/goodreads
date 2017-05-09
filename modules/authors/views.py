from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import Author
from .serializers import AuthorSerializer
from rest_framework.permissions import IsAuthenticated
from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope
# Create your views here.

class ListAuthor(APIView):
    permission_classes = (TokenHasReadWriteScope,IsAuthenticated)
    
    def get(self,request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class DetailAuthor(APIView):

    def get(self,request,pk):
        '''
        try:
            author = Author.objects.get(id=pk)
        except Exception:
            raise Http404
        '''
        author = get_object_or_404(Author,id=pk)
        serializer = AuthorSerializer(author)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def put(self,request,pk):
        author = get_object_or_404(Author,id=pk)
        serializer = AuthorSerializer(author,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        author = get_object_or_404(Author,id=pk)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
