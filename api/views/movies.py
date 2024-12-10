from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response 
from rest_framework import status
from ..models import *
from ..serializers.movie_serializer import *
from .pagination import CustomMoviePagination

@api_view(['POST'])
@permission_classes([AllowAny])
def search_movies(request):
  if 'search' not in request.data:
    return Response({
      "status": "err",
      "message": "Search parameter missing"
    }, status=status.HTTP_400_BAD_REQUEST)
  
  search_query = request.data.get('search', '')
  movies = Movie.objects.filter(title__icontains=search_query)

  if not movies.exists():
    return Response({
      "status": "err",
      "message": "No movies found matching the search criteria"
    }, status=status.HTTP_404_NOT_FOUND)
  
  total_count = movies.count()
  page_size = 5
  total_pages = (total_count + page_size - 1)
  
  paginator = CustomMoviePagination(page_size=page_size, page=1)
  paginated_movies = paginator.paginate_queryset(movies)
  serializer = MovieSearchSerializer(paginated_movies, many=True)

  return paginator.get_paginated_response(serializer.data, total_count, total_pages)

@api_view(['GET'])
@permission_classes([AllowAny])
def view_movie_detail(request, movie_id):
  movie = Movie.objects.get(pk=movie_id)
  serializer = SpecificMovieSerializer(movie)

  return Response({
    "status": "ok",
    "message": f"Here is the details for the movie {serializer.data['title']}",
    "data": serializer.data
  }, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([AllowAny])
def get_movies(request):
  page_size = request.data.get('pageSize', 10)
  page = request.data.get('page', 1)
  genre = request.data.get('genre', '')

  if genre:
    movies = Movie.objects.filter(genre=genre)
  else:
    movies = Movie.objects.all()

  total_count = movies.count()
  total_pages = (total_count + page_size - 1)

  paginator = CustomMoviePagination(page_size=page_size, page=page)
  paginated_movies = paginator.paginate_queryset(movies)
  serializer = MovieCleanSerializer(paginated_movies, many=True)

  return paginator.get_paginated_response(serializer.data, total_count, total_pages)

@api_view(['POST'])
@permission_classes([AllowAny])
def add_movie(request):
  serializer = MovieSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response({
      "status": "ok",
      "message": "Successfully added a new movie"
    }, status=status.HTTP_201_CREATED)
  
  return Response({
    "status": "err",
    "message": "Err! cannot add the the movie"
  }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([AllowAny])
def update_movie(request, movie_id):
  movie = Movie.objects.get(pk=movie_id)
  serializer = MovieSerializer(movie, data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response({
      "status": "ok",
      "message": "Movie successfully updated",
      "data": serializer.data
    }, status=status.HTTP_200_OK)
  return Response({
    "status": "err",
    "message": "Unable to update the movie details"
  }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete_movie(request):
  ids = request.data.get('ids', [])

  if not ids:
    return Response({
      "status": "err",
      "message": "Please provide a valid item id"
    }, status=status.HTTP_400_BAD_REQUEST)
  
  try:
    movie = Movie.objects.filter(id__in=ids)
    if not movie.exists():
      return Response({
        "status": "err",
        "message": "No items were found on the provided ID/s"
      }, status=status.HTTP_400_BAD_REQUEST)
    
    deleted_count = movie.delete()

    return Response({
      "status": "ok",
      "message": f"Successfully deleted {deleted_count} Movie(s)",
    }, status=status.HTTP_200_OK)
  
  except Exception as e:
    return Response({
      "status": "err",
      "message": f"An error has occurred: {str(e)}"
    }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)