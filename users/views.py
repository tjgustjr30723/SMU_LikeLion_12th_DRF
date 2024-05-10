from django.shortcuts import render
from rest_framework.response import Response
from users.models import User
from users.serializers import UserSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken
@api_view(['GET', 'POST'])
def user_list_api_view(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
@api_view(['GET', 'PUT','DELETE'])
def user_retrieve_api_view(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['POST'])
def login_api_view(request):
    if request.method =='POST':
        username = request.data.get('username')
        password = request.data.get('password')
    
        user = User.objects.get(username = username)
    
        if not check_password(password, user.password):
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        token = RefreshToken.for_user(user)
        serializer = UserSerializer(user)
        return Response(
            status=status.HTTP_200_OK,
            data={
                'token': str(token.access_token),
                'user': serializer.data,
            } #token은 객체니까 str으로 하고 위에 선언한 토큰이 아닌
             #access_token을 준다. 그리고 user의 데이터도 준다.
             #access토큰은 줘야하는 것(수명 짧음),
        )
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

 