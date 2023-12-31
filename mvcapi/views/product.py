from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from mvcapi.models import Product, User, Genre
from datetime import datetime

class ProductView(ViewSet):
    """MVC Products View"""
    
    def create(self, request):
        """POST Product"""
        
        seller_id = User.objects.get(pk=request.data["sellerId"])
        genre_id = Genre.objects.get(pk=request.data["genreId"])
        product = Product.objects.create(
            seller_id = seller_id,
            genre_id = genre_id,
            title=request.data["title"],
            description=request.data["description"],
            qty_available=request.data["qtyAvailable"],
            price=request.data["price"],
            added_on=datetime.now(),
        )
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def retrieve(self, request, pk):
        """GET Single Product"""
        
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def list(self, request):
        """GET All Products"""

        products = Product.objects.all()
        seller_id = request.query_params.get('sellerId', None)
        if seller_id is not None:
            products = products.filter(seller_id=seller_id)
        genre_id = request.query_params.get('genreId', None)
        if genre_id is not None:
            products = products.filter(genre_id=genre_id)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def update(self, request, pk):
        """PUT Product"""
        
        product = Product.objects.get(pk=pk)
        product.seller_id = User.objects.get(pk=request.data["sellerId"])
        product.genre_id = Genre.objects.get(pk=request.data["genreId"])
        product.title = request.data["title"]
        product.description = request.data["description"]
        product.qty_available = request.data["qtyAvailable"]
        product.price = request.data["price"]
        product.save()
        return Response('Product Updated', status=status.HTTP_200_OK)
    
    def destroy(self, request, pk):
        """DELETE Product"""
        
        product = Product.objects.get(pk=pk)
        product.delete()
        return Response('Product Deleted', status=status.HTTP_204_NO_CONTENT)
      
class ProductSerializer(serializers.ModelSerializer):
    """JSON Serializer for Products"""
    
    added_on = serializers.DateTimeField(format="%B %d, %Y, %I:%M%p")
    class Meta:
        model = Product
        fields = ('id', 'seller_id', 'genre_id', 'title', 'description', 'qty_available', 'price', 'added_on')
