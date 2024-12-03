from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response 
from rest_framework import status
from .models import Person
from .serializer import *
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from .pagination import CustomWishlistPagination

@api_view(['GET'])
@permission_classes([AllowAny])
def get_person(request):
  users = Person.objects.all()
  serializer = PersonSerializer(users, many=True)
  return Response({
    "status": "ok",
    "message": "Here is the list of users",
    "data": serializer.data
  })

@api_view(['POST'])
@permission_classes([AllowAny])
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


# === Wishlist ===
@api_view(['POST'])
@permission_classes([AllowAny])
def get_wishlist(request):
  page_size = request.data.get('pageSize', 10)
  page = request.data.get('page', 1)

  wishlists = Wishlist.objects.all()
  
  total_count = wishlists.count()

  total_pages = (total_count + page_size - 1)

  paginator = CustomWishlistPagination(page_size=page_size, page=page)
  
  paginated_wishlists = paginator.paginate_queryset(wishlists)

  serializer = WishlistSerializer(paginated_wishlists, many=True)

  return paginator.get_paginated_response(serializer.data, total_count, total_pages)

@api_view(['POST'])
@permission_classes([AllowAny])
def add_wishlist(request):
  serializer = WishlistSerializer(data=request.data)
  if serializer.is_valid():
    wishlist = serializer.save()
    wishlistData = WishlistSerializer(wishlist).data
    return Response({
      "status": "ok",
      "message": "successfully added a wishlist",
      "data": wishlistData
    }, status=status.HTTP_200_OK)
  
  return Response({
    "status": "err",
    "message": "Err! Cannot add the wishlist",
  }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([AllowAny])
def update_wishlist(request, pk):

  wishlist = Wishlist.objects.get(pk=pk)
  serializer = WishlistSerializer(wishlist, data=request.data)

  if serializer.is_valid():
    serializer.save()
    return Response({
      "status": "ok",
      "message": "Successfully updated the wishlist",
      "data": serializer.data
    }, status=status.HTTP_200_OK)
  
  return Response({
    "status": "err",
    "message": "Err! cannot update the wishlist"
  }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete_wishlist(request):
  ids = request.data.get('ids', [])

  if not ids:
    return Response({
      "status": "err",
      "message": "Please provide a valid item id"
    }, status=status.HTTP_400_BAD_REQUEST)
  
  try:
    wishlist = Wishlist.objects.filter(id__in=ids)
    if not wishlist.exists():
      return Response({
        "status": "err",
        "message": "No items were found on the provided ID/s"
      }, status=status.HTTP_400_BAD_REQUEST)
    
    deleted_count = wishlist.delete()

    return Response({
      "status": "ok",
      "message": f"Successfully deleted {deleted_count} wishlist(s)",
    }, status=status.HTTP_200_OK)
  
  except Exception as e:
    return Response({
      "status": "err",
      "message": f"An error has occurred: {str(e)}"
    }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# === Authentication ===
@api_view(['POST'])
@permission_classes([AllowAny])
def create_account(request):
  serializer = AccountSerializer(data=request.data)
  if serializer.is_valid():
    user = serializer.save()
    userData = UserSerializer(user).data
    refresh = RefreshToken.for_user(user)
    return Response({
      "status": "ok",
      "message": "Account is successfully created",
      "data": {
        "user": userData,
        "refresh": str(refresh),
        "token": str(refresh.access_token)
      }
    }, status=status.HTTP_201_CREATED)
  return Response({
    "status": "ok",
    "message": "Err: Account is not created"
  }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
  username = request.data.get('username')
  password = request.data.get('password')

  user = authenticate(request, username=username, password=password)

  if user is not None:
    userData = UserSerializer(user).data

    refresh = RefreshToken.for_user(user)
    
    access_token = str(refresh.access_token)
    refresh_token = str(refresh)

    return Response({
      "status": "ok",
      "message": "Login successful",
      "data": {
        "user": userData,
        "refreshToken": refresh_token,
        "accessToken": access_token
      }
    }, status=status.HTTP_200_OK)
  
  return Response({
    "status": "err",
    "message": "Invalid credentials"
  }, status=status.HTTP_401_UNAUTHORIZED)


# This logout endpoint function accepts [RefreshToken] not [AccessToken] and expires it to prevent from generatinmg new [AccessToken]
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
  try:

    refresh_token = request.data.get('refreshToken')
    
    token = RefreshToken(refresh_token)

    token.blacklist()

    return Response({
      "status": "ok",
      "message": "Logout successfull"
    }, status=status.HTTP_200_OK)
  
  except (TokenError, InvalidToken) as e:
    return Response({
      "status": "err",
      "message": f"Invalid or expired refresh token: {str(e)}"
    }, status=status.HTTP_400_BAD_REQUEST)


# === Expense Priority ===
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