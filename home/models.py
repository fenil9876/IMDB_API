from django.db import models
from django.contrib.auth.models import User
# Create your models here.(
class IMDB(models.Model):
    title=models.CharField(max_length=100)
    year=models.IntegerField(max_length=4)
    rating=models.CharField(max_length=100)
    genre=models.CharField(max_length=100)
    
class Review(models.Model):
    movie = models.ForeignKey(IMDB, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Use the imported User model
    comment = models.TextField()
    rating = models.PositiveIntegerField()


