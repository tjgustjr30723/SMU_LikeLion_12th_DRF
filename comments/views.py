from django.shortcuts import render
from rest_framework.response import Response
from users.models import User
from posts.models import Post
from comments.models import Comment
from comments.serializers import CommentSerializer
from rest_framework import status
from rest_framework.decorators import api_view
@api_view(['GET', 'POST'])
def comment_list_api_view(request):
    if request.method == 'GET':
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data, user=request.user, post=request.post)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
@api_view(['GET', 'PUT','DELETE'])
def comment_retrieve_api_view(request, comment_id):
    try:
        comment = Comment.objects.get(pk=comment_id)
    except Comment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)