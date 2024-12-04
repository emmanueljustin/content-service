from django.db import models

# Create your models here.
class Person(models.Model):
  age = models.IntegerField()
  name = models.CharField(max_length=255)

  def __str__(self):
    return self.name
  
class Wishlist(models.Model):
  itemName = models.CharField(max_length=255)
  price = models.DecimalField(max_digits=7, decimal_places=2)
  acquired = models.BooleanField()
  priorityLevel = models.IntegerField()

class ExpensePriority(models.Model):
  expenseName = models.CharField(max_length=255)
  budget = models.DecimalField(max_digits=7, decimal_places=2)
  achieved = models.BooleanField()
  priorityLevel = models.IntegerField()
  note = models.CharField(max_length=255, blank=True, null=True)
