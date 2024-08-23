from django.shortcuts import render
from django.http import request
from rest_framework.response import Response
from rest_framework.decorators import api_view,APIView
from permissions.models import Post
from permissions.serializers import PostSerializers
from rest_framework.generics import GenericAPIView,CreateAPIView
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,IsAdminUser
from permissions.permissions import IsOwnerOrViewOnly

from rest_framework.generics import ListAPIView
# Create your views here.

class PostAddList(CreateAPIView,
                  ListAPIView
                  ):
    permission_classes = [IsOwnerOrViewOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializers

class PostList(ListAPIView):
    serializer_class = PostSerializers
    queryset = Post.objects.all()


    
    


