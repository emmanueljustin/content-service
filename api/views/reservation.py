from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response 
from rest_framework import status
from ..models import *
from ..serializers.reservation_serializer import *

@api_view(['GET'])
@permission_classes([AllowAny])
def get_reservation_list(request):
  reservation = Reservation.objects.all()
  serializer = ReservationViewSerializer(reservation, many=True)
  return Response({
    "status": "ok",
    "message": "Here is the list of all the reservations",
    "data": serializer.data
  }, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([AllowAny])
def create_reservation(request):
  serializer = ReservationSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response({
      "status": "ok",
      "message": "Successfully added you reservation",
      "data": serializer.data
    }, status=status.HTTP_201_CREATED)
  return Response({
    "status": "err",
    "message": "The request you sent is invalid",
    "data": serializer.errors
  }, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['DELETE'])
# @permission_classes([AllowAny])
