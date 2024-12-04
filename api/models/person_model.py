from django.db import models

class Person(models.Model):
  age = models.IntegerField()
  name = models.CharField(max_length=255)

  def __str__(self):
    return self.name