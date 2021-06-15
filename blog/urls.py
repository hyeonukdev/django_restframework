from django.urls import path, include
from .views import BlogView, CommentView
from .api import BlogApi, BlogCreateApi, BlogUpdateApi, BlogDeleteApi
from .api import CommentApi, CommentCreateApi, CommentUpdateApi, CommentDeleteApi
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('api/',BlogApi.as_view()),
    path('api/create/',BlogCreateApi.as_view()),
    path('api/<int:pk>/',BlogUpdateApi.as_view()),
    path('api/<int:pk>/delete/',BlogDeleteApi.as_view()),

    path('comment/api/',CommentApi.as_view()),
    path('comment/api/create/',CommentCreateApi.as_view()),
    path('comment/api/<int:pk>/',CommentUpdateApi.as_view()),
    path('comment/api/<int:pk>/delete/',CommentDeleteApi.as_view()),
]