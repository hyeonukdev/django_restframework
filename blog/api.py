from rest_framework import generics
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .serializer import BlogSerializer, CommentSerializer
from .models import Blog, Comment

# ------------------------------------
# BLOG


@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
class BlogCreateApi(generics.CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


@permission_classes((IsAuthenticatedOrReadOnly,))
@authentication_classes((JSONWebTokenAuthentication,))
class BlogApi(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
class BlogUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
class BlogDeleteApi(generics.DestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


# ------------------------------------
# COMMENT

@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
class CommentCreateApi(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


@permission_classes((IsAuthenticatedOrReadOnly,))
@authentication_classes((JSONWebTokenAuthentication,))
class CommentApi(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
class CommentUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
class CommentDeleteApi(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer