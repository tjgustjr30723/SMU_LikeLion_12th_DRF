from rest_framework.response import Response
from users.models import User
from posts.models import Post
from posts.serializers import PostSerializer
from rest_framework import status
from rest_framework.decorators import api_view
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
#게시글 관리
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

#좋아요 
@api_view(['POST'])
def likes_api_view(request, post_id):
        post = Post.objects.get(pk=post_id)
        user = request.user
        if user in post.likes.all():
            post.likes.remove(user)
            return Response({'message': '게시글 좋아요를 취소했습니다.'}, status=status.HTTP_400_BAD_REQUEST)
        post.likes.add(user)
        return Response({'message': '게시글을 좋아요 했습니다.'}, status=status.HTTP_200_OK)
#특정 유저 게시글 목록 나열()
@api_view(['GET'])
def users_post_api_view(request, user_id):
    try:
        user = User.objects.get(pk=user_id)  # 해당 유저를 가져옵니다.
        posts = user.posts.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    except User.DoesNotExist:
        return Response({'message': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)
