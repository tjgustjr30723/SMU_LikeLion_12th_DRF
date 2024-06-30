from rest_framework.response import Response
from users.models import User
from posts.models import Post
from posts.serializers import PostSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import (ListCreateAPIView,RetrieveUpdateDestroyAPIView,ListAPIView)
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly
#게시글 전체 확인, 게시글 생성
class PostListCreateAPIView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
#게시글 확인, 수정, 삭제
class PostRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'post_id'
    permission_classes = [IsOwnerOrReadOnly]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.view_count += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

#좋아요 
class LikesAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'post_id'
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    def get(self, request, *args, **kwargs):
        post = self.get_object()
        user = request.user
        if user in post.likes.all():
            post.likes.remove(user)
            return Response({'message': '게시글 좋아요를 취소했습니다.'}, status=status.HTTP_200_OK)
        else:
            post.likes.add(user)
            return Response({'message': '게시글을 좋아요 했습니다.'}, status=status.HTTP_200_OK)
        
#특정 유저 게시글 목록 나열()
class UserPostsAPIView(ListAPIView):
    serializer_class = PostSerializer
    
    def get_queryset(self):
        return self.request.user.posts.all()
    



    
#----------------------------------------------------------------------------------------  
# fbv 구현 코드 
@api_view(['GET', 'POST'])
def post_list_api_view(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    #게시글 올리기
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

# 게시글 관리
@api_view(['GET','PUT','PATCH','DELETE'])
def post_retrieve_api_view(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # 게시글 조회
    if request.method == 'GET':
        #게시글 조회시 조회수 증가
        post.view_count += 1
        post.save()
        serializer = PostSerializer(post)
        return Response(serializer.data)
    #게시글 수정 및 삭제 부분은 해당 게시글 작성자만 다룰 수 있도록 구현함
    elif request.method == 'PUT':
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():

            if post.user == request.user:
                serializer.save(user=request.user)
                return Response(serializer.data)
            else:
                return Response({'message': 'You are not authorized'}, status=status.HTTP_403_FORBIDDEN)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():

            if post.user == request.user:
                serializer.save(user=request.user)
                return Response(serializer.data)
            else:
                return Response({'message': 'You are not authorized'}, status=status.HTTP_403_FORBIDDEN)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #게시글 삭제
    elif request.method == 'DELETE':
        if post.user == request.user:
            post.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'message': 'You are not authorized'}, status=status.HTTP_403_FORBIDDEN)

# 좋아요 
@api_view(['GET'])
def likes_api_view(request, post_id):
        post = Post.objects.get(pk=post_id)
        user = request.user
        if user in post.likes.all():
            post.likes.remove(user)
            return Response({'message': '게시글 좋아요를 취소했습니다.'}, status=status.HTTP_400_BAD_REQUEST)
        post.likes.add(user)
        return Response({'message': '게시글을 좋아요 했습니다.'}, status=status.HTTP_200_OK)
