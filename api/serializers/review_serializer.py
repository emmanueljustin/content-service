from rest_framework import serializers
from ..models import *

class ReviewsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Reviews
    fields = '__all__'