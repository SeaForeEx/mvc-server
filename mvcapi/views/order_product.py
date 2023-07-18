from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from mvcapi.models import OrderProduct, Order, Product

class OrderProductView(ViewSet):
    """MVC Order Products View"""
    
    def create(self, request):
        """POST Order Product"""
        
        order_id = Order.objects.get(pk=request.data["orderId"])
        product_id = Product.objects.get(pk=request.data["productId"])
        order_product = OrderProduct.objects.create(
            order_id = order_id,
            product_id = product_id,
            title=request.data["title"],
            quantity=request.data["quantity"],
            qty_total=request.data["qtyTotal"],
        )
        serializer = OrderProductSerializer(order_product)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def retrieve(self, request, pk):
        """GET Single Order Product"""
        
        order_product = OrderProduct.objects.get(pk=pk)
        serializer =OrderProductSerializer(order_product)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def list(self, request):
        """GET All Order Products"""

        order_products = Product.objects.all()
        serializer = OrderProductSerializer(order_products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def update(self, request, pk):
        """PUT Order Product"""
        
        order_product = Product.objects.get(pk=pk)
        order_product.quantity = request.data["quantity"]
        order_product.qtyTotal = request.data["qtyTotal"]
        order_product.save()
        return Response('Order Product Updated', status=status.HTTP_200_OK)
    
    def destroy(self, request, pk):
        """DELETE Order"""
        
        order_product = OrderProduct.objects.get(pk=pk)
        order_product.delete()
        return Response('Order Product Deleted', status=status.HTTP_204_NO_CONTENT)
      
class OrderProductSerializer(serializers.ModelSerializer):
    """JSON Serializer for Order Products"""
    
    class Meta:
        model = OrderProduct
        fields = ('id', 'order_id', 'product_id', 'title', 'quantity', 'qty_total')
