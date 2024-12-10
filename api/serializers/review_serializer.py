from rest_framework import serializers
from ..models import *

class ReviewsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Reviews
    fields = '__all__'
 
# Used in resposne to reove the movie id along with the response
class ReviewsCleanSerializer(serializers.ModelSerializer):
  class Meta:
    model = Reviews
    fields = ['name', 'createdAt', 'review', 'individualRating']