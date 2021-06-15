from rest_framework import generics
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .serializer import BlogSerializer
from .models import Blog


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
