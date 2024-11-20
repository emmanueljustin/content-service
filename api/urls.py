from django.urls import path
from .views import get_user, add_user, update_user, remove_user

urlpatterns = [
  path('users/', get_user, name='get_user'),
  path('users/add/', add_user, name='add_user'),
  path('users/update/<int:pk>/', update_user, name='update_user'),
  path('users/remove/<int:pk>/', remove_user, name='remove_user')
]