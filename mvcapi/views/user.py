from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from mvcapi.models import User

class UserView(ViewSet):
    """MVC Users View"""
    
    def create(self, request):
        """CREATE User"""
        
        user = User.objects.create(
            user_name=request.data["userName"],
            email=request.data["email"],
            profile_image_url=request.data["profileImageUrl"],
            bio=request.data["bio"],
            uid=request.data["uid"],
        )
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def retrieve(self, request, pk):
        """GET Single User"""
        
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
    
    def list(self, request):
        """GET All Users"""

        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def update(self, request, pk):
        """PUT Order"""
        
        user = User.objects.get(pk=pk)
        user.user_name = request.data["userName"]
        user.email=request.data["email"]
        user.profile_image_url=request.data["profileImageUrl"]
        user.bio = request.data["bio"]
        user.save()
        return Response('User Updated', status=status.HTTP_200_OK)
      
class UserSerializer(serializers.ModelSerializer):
    """JSON Serializer for Users"""
    
    class Meta:
        model = User
        fields = ('id', 'user_name', 'email', 'profile_image_url', 'bio', 'uid')
