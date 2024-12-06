from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response 
from rest_framework import status
from ..serializers.review_serializer import *
from ..models import *

@api_view(['POST'])
@permission_classes([AllowAny])
def post_review(request, movie_id):
  try:
    movie = Movie.objects.get(id=movie_id)

  except Movie.DoesNotExist:
    return Response({
      "status": "err",
      "message": "Movie not found"
    }, status=status.HTTP_404_NOT_FOUND)
  
  review_data = request.data
  review_data['movie'] = movie.id

  serializer = ReviewsSerializer(data=review_data)

  if serializer.is_valid():
    review = serializer.save()
    reviewData = ReviewsSerializer(review).data
    return Response({
      "status": "ok",
      "message": f"Successfully added a review for {movie.title}"
    }, status=status.HTTP_201_CREATED)
  
  return Response({
    "status": "err",
    "message": "Invalid request"
  }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([AllowAny])
def update_review(request, review_id):
  review = Reviews.objects.get(pk=review_id)
  serializer = ReviewsSerializer(review, data=request.data)

  if serializer.is_valid():
    serializer.save()
    return Response({
      "status": "ok",
      "message": "Successfully updated the review",
      "data": serializer.data
    }, status=status.HTTP_200_OK)
  
  else:
    return Response({
      "status": "err",
      "message": "Err! review data is not updated"
    }, status=status.HTTP_400_BAD_REQUEST)
  
@api_view(['DELETE'])
@permission_classes([AllowAny])
def remove_review(request, review_id):
  review = Reviews.objects.get(pk=review_id)
  review.delete()
  return Response({
    "status": "ok",
    "message": "The review is successfully removed"
  }, status=status.HTTP_200_OK)