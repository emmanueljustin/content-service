from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response 
from rest_framework import status
from ..serializer import *

@api_view(['GET'])
@permission_classes([AllowAny])
def get_expense(request):
  expense = ExpensePriority.objects.all()
  serializer = ExpensePrioritySerializer(expense, many=True)
  return Response({
    "status": "ok",
    "message": "Here is the list of expenses masayaka na?",
    "data": serializer.data
  })

@api_view(['POST'])
@permission_classes([AllowAny])
def add_expense(request):
  serializer = ExpensePrioritySerializer(data=request.data)
  if serializer.is_valid():
    expense = serializer.save()
    expenseData = ExpensePrioritySerializer(expense).data
    return Response({
      "status": "ok",
      "message": "successfully added a expense",
      "data": expenseData
    }, status=status.HTTP_200_OK)