from django.urls import path
from .views import get_person, add_person, update_person, remove_person

urlpatterns = [
  path('persons/', get_person, name='get_person'),
  path('persons/add/', add_person, name='add_person'),
  path('persons/update/<int:pk>/', update_person, name='update_person'),
  path('persons/remove/<int:pk>/', remove_person, name='remove_person')
]