from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response 
from rest_framework import status
from ..serializers.wishlist_serializer import *
from ..pagination import CustomWishlistPagination

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