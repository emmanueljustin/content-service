from rest_framework import serializers
from .models import Person, Wishlist
from django.contrib.auth.models import User

class PersonSerializer(serializers.ModelSerializer):
  class Meta:
    model = Person
    fields = '__all__'

class WishlistSerializer(serializers.ModelSerializer):
  class Meta:
    model = Wishlist
    fields = '__all__'
    

# Authentication
class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['username', 'email']

class AccountSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['username', 'email', 'password']

  def create(self, validated_data):
    user = User.objects.create_user(**validated_data)
    return user