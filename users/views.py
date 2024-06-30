from django.shortcuts import render
from rest_framework.response import Response
from users.models import User
from users.serializers import UserSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken
import string
import random
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from .permissions import IsOwnerOrReadOnly
# 유서 생성, 확인
class UserListCreateAPIView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
# 프로필 보기, 수정 및 삭제
class ProfileAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    def get_object(self):
        return self.request.user
# 로그인
class LoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        if not check_password(password, user.password):
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        token = RefreshToken.for_user(user)
        serializer = UserSerializer(user)
        return Response(
            status=status.HTTP_200_OK,
            data={
                'token': str(token.access_token),
                'user': serializer.data,
            }
        )

# 비밀번호 변경
class ChangePasswordAPIView(APIView):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def patch(self, request):
        user = request.user
        old_password = request.data.get('old_password')
        new_password = request.data.get('new_password')
        # 기존 비밀번호 확인
        if not check_password(old_password, user.password):
            return Response({'message': 'Invalid old password'}, status=status.HTTP_400_BAD_REQUEST)
        # 새로운 비밀번호 설정
        user.set_password(new_password)
        user.save()
        return Response({'message': 'Password changed successfully'}, status=status.HTTP_200_OK)
    
#비밀번호 재설정(원래는 이메일을 입력하면 해당 이메일이 존재할 때 그 이메일로 비밀번호를 재설정할 수 있는 링크를 보낼려고 했으나, 어려워서 간단하게 만들었습니다.)
class ResetPasswordAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        try:
            user = User.objects.get(username=username, email=email)
        except User.DoesNotExist:
            return Response({'message': 'Username and email do not match'}, status=status.HTTP_404_NOT_FOUND)
        new_password = self.recreate_password()
        user.set_password(new_password)
        user.save()
        return Response({'message': 'Temporary password: {}'.format(new_password)}, status=status.HTTP_200_OK)
    def recreate_password(self):
        letters_and_digits = string.ascii_letters + string.digits
        new_password = ''.join(random.choice(letters_and_digits) for i in range(8))
        return new_password

#----------------------- fbv------------------------------------------
@api_view(['GET', 'POST'])
def user_list_api_view(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    #회원가입
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PATCH', 'DELETE'])
def profile_api_view(request):
    user = request.user
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'PATCH':
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)
    
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
@api_view(['PATCH'])
def change_password_api_view(request):
    user = request.user 
    old_password = request.data.get('old_password')
    new_password = request.data.get('new_password')

    # 기존 비밀번호 확인
    if not check_password(old_password, user.password):
        return Response({'message': 'Invalid old password'}, status=status.HTTP_400_BAD_REQUEST)
    # 새로운 비밀번호 설정
    user.set_password(new_password)
    user.save()
    return Response({'message': 'Password changed successfully'}, status=status.HTTP_200_OK)

@api_view(['POST'])
def reset_password_api_view(request):
    if request.method == 'POST':
        username = request.data.get('username')
        email = request.data.get('email')
        try:
            user = User.objects.get(username=username, email=email)
        except User.DoesNotExist:
            return Response({'message': 'Username and email do not match'}, status=status.HTTP_404_NOT_FOUND)
        new_password = recreate_password()
        user.set_password(new_password)
        user.save()
        return Response({'message': 'Temporary password: {}'.format(new_password)}, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

def recreate_password():
    letters_and_digits = string.ascii_letters + string.digits
    new_password = ''.join(random.choice(letters_and_digits) for i in range(8))
    return new_password
#-------------------------------------------------------------------------
