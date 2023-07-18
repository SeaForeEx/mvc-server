from django.db import models

class User(models.Model):
    """Model that represents a user"""
    user_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    profile_image_url = models.CharField(max_length=1000)
    bio = models.CharField(max_length=5000)
    uid = models.CharField(max_length=50)
