from rest_framework import serializers
from ..models import *

class ReviewsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Reviews
    fields = '__all__'
 
# Used in resposne to remove the movie id along with the response
class ReviewsCleanSerializer(serializers.ModelSerializer):
  class Meta:
    model = Reviews
    fields = ['id', 'name', 'createdAt', 'review', 'individualRating']