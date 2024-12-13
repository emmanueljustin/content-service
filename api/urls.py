from django.urls import path
from .views.person import *
from .views.wishlist import *
from .views.authentication import *
from .views.expense import *
from .views.movies import *
from .views.reviews import *
from .views.reservation import *

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
  path('auth/user/', get_user_details, name='get_user_details'),
  path('auth/logout/', logout, name='logout'),

  # Expense Priority
  path('expense/', get_expense, name='get_expense'),
  path('expense/add/<int:person_id>', add_expense, name='add_expense'),
  path('expense/update/<int:pk>/', update_expense, name='update_expense'),
  path('expense/delete/', delete_expenses, name='delete_expenses'),

  # Movie
  path('movie/search/', search_movies, name='search_movies'),
  path('movie/detail/<int:movie_id>', view_movie_detail, name='view_movie_detail'),
  path('movie/', get_movies, name='get_movies'),
  path('movie/add/', add_movie, name='add_movie'),
  path('movie/update/<int:movie_id>', update_movie, name='update_movie'),
  path('movie/delete/', delete_movie, name='delete_movie'),

  # Reservation
  path('reservation/', get_reservation_list, name='get_reservation_list'),
  path('reservation/create/', create_reservation, name='create_reservation'),

  # Reviews
  path('review/post/<int:movie_id>', post_review, name='post_review'),
  path('review/update/<int:review_id>', update_review, name='update_review'),
  path('review/delete/<int:review_id>', remove_review, name='remove_review'),
]