from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Author
from .serializers import AuthorSerializer
# Create your views here.

class ListAuthor(APIView):

    def get(self,request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        pass

class DetailAuthor(APIView):

    def get(self,request):
        pass
    def put(self,request):
        pass
    def delete(self,request):
        pass
