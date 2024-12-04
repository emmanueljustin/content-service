from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response 
from rest_framework import status
from ..serializers.expense_serializer import *
from ..models.expense_model import ExpensePriority

@api_view(['GET'])
@permission_classes([AllowAny])
def get_expense(request):
  expense = ExpensePriority.objects.all()
  serializer = ExpensePrioritySerializer(expense, many=True)
  return Response({
    "status": "ok",
    "message": "Here is the list of expenses",
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
  
@api_view(['PUT'])
@permission_classes([AllowAny])
def update_expense(request, pk):
  expense = ExpensePriority.objects.get(pk=pk)
  serializer = ExpensePrioritySerializer(expense, data=request.data)

  if serializer.is_valid():
    serializer.save()
    return Response({
      "status": "ok",
      "message": "Successfully updated the expense data",
      "data": serializer.data
    }, status=status.HTTP_200_OK)
  
  else:
    return Response({
      "status": "err",
      "message": "Err! expense data is not updated"
    }, status=status.HTTP_400_BAD_REQUEST)
  
@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete_expenses(request):
  ids = request.data.get('ids', [])

  if not ids:
    return Response({
      "status": "err",
      "message": "Please provide valid ids"
    }, status=status.HTTP_400_BAD_REQUEST)
  
  try:
    expense = ExpensePriority.objects.filter(id__in=ids)

    if not expense.exists():
      return Response({
        "status": "err",
        "message": "there are no items found on the provided ids"
      }, status=status.HTTP_400_BAD_REQUEST)
    
    deleted_items = expense.delete()

    return Response({
      "status": "ok",
      "message": f"Successfully deleted {deleted_items} expense(s)",
    }, status=status.HTTP_200_OK)

  except Exception as e:
    return Response({
      "status": "err",\
      "message": f"An error has occured: {str(e)}"
    }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
