
from rest_framework.response import Response
from users.models import User
from posts.models import Post
from comments.models import Comment
from comments.serializers import CommentSerializer
from rest_framework import status
from rest_framework.decorators import api_view
@api_view(['GET'])
def comment_list_api_view(request):
    #댓글 확인
    if request.method == 'GET':
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    #댓글 추가
@api_view(['POST'])
def comment_m_api_view(request,post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(user=request.user, post=post)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET', 'PATCH','DELETE'])
def comment_retrieve_api_view(request, comment_id):
    try:
        comment = Comment.objects.get(pk=comment_id)
    except Comment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
    elif request.method == 'PATCH':
        serializer = CommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid():

            if comment.user == request.user:
                serializer.save(user=request.user)
                return Response(serializer.data)
            else:
                return Response({'message': 'You are not authorized'}, status=status.HTTP_403_FORBIDDEN)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#댓글 좋아요
@api_view(['POST'])
def likes_api_view(request, comment_id):
        try:
            comment = Comment.objects.get(pk=comment_id)
        except Comment.DoesNotExist:
             return Response({'message':'해당 댓글이 존재하지 않습니다.'}, status=status.HTTP_404_NOT_FOUND)
        user = request.user
        if user in comment.likes.all():
            comment.likes.remove(user)
            return Response({'message': '댓글 좋아요를 취소했습니다.'}, status=status.HTTP_200_OK)
        comment.likes.add(user)
        return Response({'message': '댓글을 좋아요 했습니다.'}, status=status.HTTP_200_OK)