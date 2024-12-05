from django.db import models

class Movies(models.Model):
  title = models.CharField(max_length=100)
  synopsis = models.CharField(max_length=255)
  genre = models.CharField(max_length=255)
  rating = models.IntegerField()
