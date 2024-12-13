from django.db import models
from .movies_model import Movie
from .person_model import Person

# dateReserved:

# Type: DateTimeField
# Accepts a specific date and time for when the reservation is made.
# You must provide a datetime value for this field, like [2024-12-13 15:30:00].

class Reservation(models.Model):
  reservedAt = models.DateTimeField(auto_now_add=True)
  price = models.DecimalField(max_digits=6, decimal_places=2)
  dateReserved = models.DateTimeField()
  person = models.OneToOneField(Person, related_name='reservedTo', blank=True, on_delete=models.CASCADE)
  movie = models.OneToOneField(Movie, related_name='reservedMovie', blank=True, on_delete=models.CASCADE)
  # Will add status status to check if the reservation is canceled or not
  # status = models