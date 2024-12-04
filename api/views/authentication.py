from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from ..serializers.auth_serializer import *
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken

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