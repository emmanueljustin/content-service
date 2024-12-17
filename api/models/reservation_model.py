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
  person = models.ForeignKey(Person, related_name='reservedTo', blank=True, on_delete=models.CASCADE)
  movie = models.ForeignKey(Movie, related_name='reservedMovie', blank=True, on_delete=models.CASCADE)
  status = models.CharField(max_length=100)

  class Meta:
    constraints = [
      models.UniqueConstraint(fields=['person', 'movie'], name='unique_reservation')
    ]