from django.urls import path, include
from .api import StudentCreateApi, StudentApi, StudentUpdateApi, StudentDeleteApi

urlpatterns = [
    path('api',StudentCreateApi.as_view()),
    path('api/create',StudentCreateApi.as_view()),
    path('api/<int:pk>',StudentUpdateApi.as_view()),
    path('api/<int:pk>/delete',StudentDeleteApi.as_view()),
]