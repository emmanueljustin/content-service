from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CustomWishlistPagination(PageNumberPagination):
  def __init__(self, page_size, page, max_page_size=100):
    self.page_size = page_size
    self.page = page
    self.max_page_size = max_page_size

  def paginate_queryset(self, queryset):
    self.page_size = min(self.page_size, self.max_page_size)
    
    start = (self.page - 1) * self.page_size
    end = start + self.page_size
    
    return queryset[start:end]

  def get_paginated_response(self, data, total_count, total_pages):
    total_pages = (total_count + self.page_size - 1) // self.page_size
    
    return Response({
        'status': 'ok',
        'message': 'Here is the list of wishlist',
        'data': data,
        'count': total_count,
        'total_pages': total_pages,
        'next': self.page + 1 if self.page < total_pages else None,
        'previous': self.page - 1 if self.page > 1 else None,
    })