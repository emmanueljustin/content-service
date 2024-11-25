from django.urls import path
from .views import *

urlpatterns = [
  path('persons/', get_person, name='get_person'),
  path('persons/add/', add_person, name='add_person'),
  path('persons/update/<int:pk>/', update_person, name='update_person'),
  path('persons/remove/<int:pk>/', remove_person, name='remove_person'),

  # Wishlist
  path('wishlist/', get_wishlist, name='get_wishlist'),
  path('wishlist/add/', add_wishlist, name='add_wishlist'),
  path('wishlist/update/<int:pk>/', update_wishlist, name='update_wishlist'),
  path('wishlist/delete/', delete_wishlist, name='delete_wishlist'),
  
  # Authentication
  path('auth/register/', create_account, name='create_account'),
  path('auth/login/', login, name='login'),
  path('auth/logout/', logout, name='logout'),
]