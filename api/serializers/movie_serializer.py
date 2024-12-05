from rest_framework import serializers

from ..serializers.review_serializer import ReviewsSerializer
from ..models import *

class MovieSerializer(serializers.ModelSerializer):
  reviews = ReviewsSerializer(many=True, required=False)
  class Meta:
    model = Movies
    fields = ['id', 'title', 'synopsis', 'genre', 'rating', 'reviews']