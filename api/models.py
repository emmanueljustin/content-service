from django.db import models

# Create your models here.
class User(models.Model):
  age = models.IntegerField()
  name = models.CharField(max_length=255)

  def __str__(self):
    return self.name