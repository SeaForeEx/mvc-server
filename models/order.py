from django.db import models
from .user import User

class Order(models.Model):
    """Model that represents an order"""
    customer_id = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_type = models.CharField(max_length=50)
    is_open = models.BooleanField()
    total = models.IntegerField()
