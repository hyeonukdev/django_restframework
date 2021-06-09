from django.shortcuts import render
from .serializers import UserSerializer, SuperUserSerializer
from .models import User
from rest_framework import generics

# -------------------------------------
# normalUser

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all().filter(is_admin=False)
    serializer_class = UserSerializer


class UserUpdate(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDelete(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# -------------------------------------
# superUser


class SuperUserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SuperUserSerializer


class SuperUserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = SuperUserSerializer


class SuperUserUpdate(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = SuperUserSerializer


class SuperUserDelete(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = SuperUserSerializer