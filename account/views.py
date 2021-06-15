from django.shortcuts import render
from .serializers import UserSerializer, SuperUserSerializer
from .models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.decorators import permission_classes


# -------------------------------------
# normalUser


@permission_classes((AllowAny, ))
class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all().filter(is_admin=False)
    serializer_class = UserSerializer


class UserUpdate(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all().filter(is_admin=False)
    serializer_class = UserSerializer


class UserDelete(generics.DestroyAPIView):
    queryset = User.objects.all().filter(is_admin=False)
    serializer_class = UserSerializer


# -------------------------------------
# superUser


@permission_classes((AllowAny, ))
class SuperUserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SuperUserSerializer


@permission_classes((IsAdminUser, ))
class SuperUserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = SuperUserSerializer


@permission_classes((IsAdminUser, ))
class SuperUserUpdate(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = SuperUserSerializer


@permission_classes((IsAdminUser, ))
class SuperUserDelete(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = SuperUserSerializer