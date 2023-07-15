from django.db import models
from models import User, Genre

class Product(models.Model):
    seller_id = models.ForeignKey(User, on_delete=models.CASCADE)
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    qtyAvailable = models.IntegerField()
    price = models.IntegerField()
    added_on = models.DateTimeField()
