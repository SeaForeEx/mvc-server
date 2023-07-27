from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from mvcapi.models import Order, User

class OrderView(ViewSet):
    """MVC Orders View"""
    
    def create(self, request):
        """POST Order"""
        
        customer_id = User.objects.get(pk=request.data["customerId"])
        order = Order.objects.create(
            customer_id = customer_id,
            payment_type=request.data["paymentType"],
            is_open=request.data["isOpen"],
            total=request.data["total"],
        )
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def retrieve(self, request, pk):
        """GET Single Order"""
        
        order = Order.objects.get(pk=pk)
        customer_id = request.query_params.get('customerId', None)
        if customer_id is not None:
            order = order.filter(customer_id=customer_id)
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def list(self, request):
        """GET All Orders"""

        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def update(self, request, pk):
        """PUT Order"""
        
        order = Order.objects.get(pk=pk)
        order.customer_id = User.objects.get(pk=request.data["customerId"])
        order.payment_type = request.data["paymentType"]
        order.is_open = request.data["isOpen"]
        order.total = request.data["total"]
        order.save()
        return Response('Order Updated', status=status.HTTP_200_OK)
    
    def destroy(self, request, pk):
        """DELETE Order"""
        
        order = Order.objects.get(pk=pk)
        order.delete()
        return Response('Order Deleted', status=status.HTTP_204_NO_CONTENT)
      
class OrderSerializer(serializers.ModelSerializer):
    """JSON Serializer for Orders"""
    
    class Meta:
        model = Order
        fields = ('id', 'customer_id', 'payment_type', 'is_open', 'total')
