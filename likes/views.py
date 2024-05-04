from django.shortcuts import render
from rest_framework.response import Response
from likes.models import Like
from comments.models import Comment
from likes.serializers import LikeSerializer
from rest_framework import status
from rest_framework.decorators import api_view
@api_view(['GET', 'POST'])
def like_list_api_view(request):
    if request.method == 'GET':
        likes = Like.objects.all()
        serializer = LikeSerializer(likes, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = LikeSerializer(data=request.data, user=request.user, post=request.post, comment=request.comment)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
@api_view(['GET', 'PUT','DELETE'])
def like_retrieve_api_view(request, pk):
    try:
        like = Like.objects.get(pk=pk)
    except Like.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = LikeSerializer(like)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = LikeSerializer(like, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        like.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)