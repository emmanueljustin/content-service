from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializer import UserSerializer

@api_view(['GET'])
def get_user(request):
  users = User.objects.all()
  serializer = UserSerializer(users, many=True)
  return Response({
    "status": "ok",
    "message": "Here is the list of users",
    "data": serializer.data
  })

@api_view(['POST'])
def add_user(request):
  serializer = UserSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_user(request, pk):
  user = User.objects.get(pk=pk)
  serializer = UserSerializer(user, data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response({
      "status": "ok",
      "message": "User successfully updated",
      "data": serializer.data
    }, status=status.HTTP_200_OK)
  return Response({
    "status": "err",
    "message": "Unable to update the user data"
  }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def remove_user(request, pk):
  user = User.objects.get(pk=pk)
  user.delete()
  return Response({
    "status": "ok",
    "message": "The User is successfully removed"
  }, status=status.HTTP_200_OK)