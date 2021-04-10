from django.shortcuts import render
#generics views
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView

#define classes
from blog.serializers import PostSerializer
from blog.models import Post


#create
class ListPostAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CreatePostAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UpdatePostAPIView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class DeletePostAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


