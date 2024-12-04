from rest_framework import serializers
from ..models import ExpensePriority

class ExpensePrioritySerializer(serializers.ModelSerializer):
  class Meta:
    model = ExpensePriority
    fields = '__all__'