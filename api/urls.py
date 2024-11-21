from django.urls import path
from .views import *

urlpatterns = [
  path('persons/', get_person, name='get_person'),
  path('persons/add/', add_person, name='add_person'),
  path('persons/update/<int:pk>/', update_person, name='update_person'),
  path('persons/remove/<int:pk>/', remove_person, name='remove_person'),

  # Authentication
  path('auth/register/', create_account, name='create_account'),
  path('auth/login/', login, name='login'),
  path('auth/logout/', logout, name="logout"),
]