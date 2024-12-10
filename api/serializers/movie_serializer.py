from rest_framework import serializers

from ..serializers.review_serializer import ReviewsSerializer, ReviewsCleanSerializer
from ..models import *

class MovieSerializer(serializers.ModelSerializer):
  reviews = ReviewsSerializer(many=True, required=False)
  class Meta:
    model = Movie
    fields = ['id', 'title', 'synopsis', 'genre', 'rating', 'reviews']

  def create(self, validated_data):
    reviews_data = validated_data.pop('reviews', [])
    movie = Movie.objects.create(**validated_data)

    for review_data in reviews_data:
      Reviews.objects.create(movie=movie, **review_data)
    
    return movie
  
# Used only for fetching clean reviews when getting a list of movies
class MovieCleanSerializer(serializers.ModelSerializer):
  class Meta:
    model = Movie
    fields = ['id', 'title', 'synopsis', 'genre', 'rating']

# Used for getting a single specific movie detail
class SpecificMovieSerializer(serializers.ModelSerializer):
  reviews = ReviewsCleanSerializer(many=True, required=False)
  class Meta:
    model = Movie
    fields = ['id', 'title', 'synopsis', 'genre', 'rating', 'reviews']

# Used for limiting the data shown in response when searching for movies
class MovieSearchSerializer(serializers.ModelSerializer):
  class Meta:
    model = Movie
    fields = ['id', 'title']