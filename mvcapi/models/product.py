from django.db import models
from .user import User
from .genre import Genre

class Product(models.Model):
    seller_id = models.ForeignKey(User, on_delete=models.CASCADE)
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    qty_available = models.IntegerField()
    price = models.IntegerField()
    added_on = models.DateTimeField()
