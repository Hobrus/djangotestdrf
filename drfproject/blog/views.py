from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from rest_framework import viewsets, permissions, mixins
from rest_framework.permissions import BasePermission
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet

from .filters import PostFilter
from .models import Post
from .serializers import PostsSerializer


# Create your views here.
class PostsViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostsSerializer
    # /api/posts/?title=Hello
    filterset_class = PostFilter
    # /api/posts/?ordering=-created_at descending order
    ordering_fields = ['created_at']
    # /api/posts/?search=Hello
    search_fields = ['title', 'content']

    # /api/posts/1/hello а так по имени функции
    @action(detail=True, methods=['GET'])
    def hello(self, request, pk=None):
        posts = Post.objects.all()
        serializer = PostsSerializer(posts, many=True)
        return HttpResponse(serializer.data)

    # /api/posts/hello а так по имени функции
    @action(detail=False, methods=['GET'])
    def hello(self, request):
        return HttpResponse('Hello')

    # def create(self, request, *args, **kwargs):
    #     # здесь логика до
    #     response = super().create(request, *args, **kwargs)
    #     # здесь после создания
    #     return response

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        # здесь мы можем описать логику транзакции
        return super().create(request, *args, **kwargs)