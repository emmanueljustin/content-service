from rest_framework import serializers

from ..serializers.expense_serializer import ExpensePrioritySerializer
from ..models import *

class PersonSerializer(serializers.ModelSerializer):
  expenses = ExpensePrioritySerializer(many=True, required=False)
  class Meta:
    model = Person
    fields = ['id', 'age', 'name', 'expenses']

  def create(self, validated_data):
    expenses_data = validated_data.pop('expenses', [])
    person = Person.objects.create(**validated_data)

    for expense_data in expenses_data:
      ExpensePriority.objects.create(person=person, **expense_data)

    return person