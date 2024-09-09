from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer
    


class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer




"""
https://www.django-rest-framework.org/api-guide/generic-views/
Here, we have all the different types of RetrieveDestroyAPIView


1. RetrieveDestroyAPIView
2. ListCreateAPIView
3. RetrieveAPIView


There are these different types of views with which we can use the different ways to use the methods
"""