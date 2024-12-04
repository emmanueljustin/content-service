from django.db import models

class ExpensePriority(models.Model):
  expenseName = models.CharField(max_length=255)
  budget = models.DecimalField(max_digits=7, decimal_places=2)
  achieved = models.BooleanField()
  priorityLevel = models.IntegerField()
  note = models.CharField(max_length=255, blank=True, null=True)