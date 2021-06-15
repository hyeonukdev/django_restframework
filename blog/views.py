from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse

from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Blog, Comment
from .serializer import BlogSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly


class BlogView(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    # permission 추가
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    # serializer.save() 재정의
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentView(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)


@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
@authentication_classes((JSONWebTokenAuthentication,))
def posts(request):
    posts = Blog.objects.filter(
        published_at__isnull=False).order_by('-published_at')
    post_list = serializers.serialize('json', posts)
    return HttpResponse(post_list, content_type="text/json-comment-filtered")