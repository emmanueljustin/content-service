from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Person
from .serializer import PersonSerializer

@api_view(['GET'])
def get_person(request):
  users = Person.objects.all()
  serializer = PersonSerializer(users, many=True)
  return Response({
    "status": "ok",
    "message": "Here is the list of users",
    "data": serializer.data
  })

@api_view(['POST'])
def add_person(request):
  serializer = PersonSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_person(request, pk):
  user = Person.objects.get(pk=pk)
  serializer = PersonSerializer(user, data=request.data)
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
def remove_person(request, pk):
  user = Person.objects.get(pk=pk)
  user.delete()
  return Response({
    "status": "ok",
    "message": "The User is successfully removed"
  }, status=status.HTTP_200_OK)