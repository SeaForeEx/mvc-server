from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from mvcapi.models import Genre

class GenreView(ViewSet):
    """MVC Genres View"""
    
    def create(self, request):
        """POST Genre"""
        
        # Create a new Genre object with the provided description from the request data
        genre = Genre.objects.create(
            description=request.data["description"],
        )
        # Serialize the genre object
        serializer = GenreSerializer(genre)
        # Return the serialized data along with the HTTP 201 Created status
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      
    def retrieve(self, request, pk):
        """GET Single Genre"""
        
        # Retrieve a single Genre object based on the provided pk (primary key)
        genre = Genre.objects.get(pk=pk)
        # Serialize the genre object
        serializer = GenreSerializer(genre)
        # Return the serialized data along with the HTTP 200 OK status
        return Response(serializer.data, status=status.HTTP_200_OK)
      
    def list(self, request):
        """GET All Genres"""
        
        # Retrieve all Genre objects
        genre = Genre.objects.all()
        # Serialize the genre objects
        serializer = GenreSerializer(genre, many=True)
        # Return the serialized data along with the HTTP 200 OK status
        return Response(serializer.data, status=status.HTTP_200_OK)
      
    def update(self, request, pk):
        """PUT Genre"""
        
        # Retrieve a single Genre object based on the provided pk
        genre = Genre.objects.get(pk=pk)
        # Update the genre's description with the new description from the request data
        genre.description = request.data["description"]
        # Save the updated genre object
        genre.save()
        # Return a response with a simple message and the HTTP 200 OK status
        return Response('Genre Updated', status=status.HTTP_200_OK)
      
    def destroy(self, request, pk):
        """DELETE Genre"""
        
        # Retrieve a single Genre object based on the provided pk
        genre = Genre.objects.get(pk=pk)
        # Delete the genre object from the database
        genre.delete()
        # Return a response with a simple message and the HTTP 204 No Content status
        return Response('Genre Deleted', status=status.HTTP_204_NO_CONTENT)
      
class GenreSerializer(serializers.ModelSerializer):
    """JSON Serializer for Genres"""
    
    class Meta:
        model = Genre
        fields = ('id', 'description')
