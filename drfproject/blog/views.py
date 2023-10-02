from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from rest_framework import viewsets, permissions
from rest_framework.permissions import BasePermission

from .models import Post
from .serializers import PostsSerializer


# Create your views here.
class PostsViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostsSerializer