from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response 
from rest_framework import status
from .pagination import CustomReservationPagination
from ..models import *
from ..serializers.reservation_serializer import *

@api_view(['POST'])
@permission_classes([AllowAny])
def get_reservation_list(request):
  page_size = request.data.get('pageSize', 10)
  page = request.data.get('page', 1)

  reservation = Reservation.objects.all()
  total_count = reservation.count()
  total_pages = (total_count + page_size - 1)

  paginator = CustomReservationPagination(page_size=page_size, page=page)
  paginated_reservations = paginator.paginate_queryset(reservation)
  serializer = ReservationViewSerializer(paginated_reservations, many=True)

  return paginator.get_paginated_response(serializer.data, total_count, total_pages)

@api_view(['POST'])
@permission_classes([AllowAny])
def create_reservation(request):
  serializer = ReservationSerializer(data=request.data)
  if serializer.is_valid():
    try:
      serializer.save()
      return Response({
        "status": "ok",
        "message": "Successfully added you reservation",
        "data": serializer.data
      }, status=status.HTTP_201_CREATED)
    except Exception as e:
      return Response({
        "status": "err",
        "message": "This person already has a reservation for this movie"
      }, status=status.HTTP_400_BAD_REQUEST)
  return Response({
    "status": "err",
    "message": "The request you sent is invalid",
    "data": serializer.errors
  }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([AllowAny])
def update_reservation_status(request, reservation_id):
  try:
    reservation = Reservation.objects.get(pk=reservation_id)
  except Reservation.DoesNotExist:
    return Response({
      "status": "err",
      "message": "Reservation not found"
    }, status=status.HTTP_404_NOT_FOUND)
  
  serializer = ReservationStatusSerializer(reservation, data=request.data, partial=True)
  viewSerializer = ReservationViewSerializer(reservation)

  if serializer.is_valid():
    serializer.save()
    return Response({
      "status": "ok",
      "message": "Reservation status is successfully updated",
      "data": viewSerializer.data,
    }, status=status.HTTP_200_OK)
  
  return Response({
    "status": "err",
    "message": serializer.errors
  })
