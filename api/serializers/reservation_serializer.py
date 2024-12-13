from rest_framework import serializers
from ..models.reservation_model import Reservation
from ..models.movies_model import Movie
from ..models.person_model import Person

class ReservationSerializer(serializers.ModelSerializer):
  person = serializers.PrimaryKeyRelatedField(queryset=Person.objects.all())
  movie = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all())
  
  class Meta:
    model = Reservation
    fields = '__all__'

class ReservationViewSerializer(serializers.ModelSerializer):
  movieName = serializers.CharField(source='movie.title')
  personName = serializers.CharField(source='person.name')

  class Meta:
    model = Reservation
    fields = ['id', 'reservedAt', 'price', 'dateReserved', 'movieName', 'personName']
