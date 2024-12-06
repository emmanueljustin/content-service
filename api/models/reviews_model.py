from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from .movies_model import Movie

class Reviews(models.Model):
  name = models.CharField(max_length=200)
  createdAt = models.DateTimeField(auto_now_add=True)
  review = models.CharField(max_length=255)
  individualRating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
  movie = models.ForeignKey(Movie, related_name='reviews', blank=True, on_delete=models.CASCADE)
