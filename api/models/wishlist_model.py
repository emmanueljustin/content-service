from django.db import models

class Wishlist(models.Model):
  itemName = models.CharField(max_length=255)
  price = models.DecimalField(max_digits=7, decimal_places=2)
  acquired = models.BooleanField()
  priorityLevel = models.IntegerField()