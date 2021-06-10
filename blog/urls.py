from django.urls import path, include
from .views import BlogViewSet
from .api import BlogApi, BlogCreateApi, BlogUpdateApi, BlogDeleteApi

urlpatterns = [
    path('api',BlogApi.as_view()),
    path('api/create',BlogCreateApi.as_view()),
    path('api/<int:pk>',BlogUpdateApi.as_view()),
    path('api/<int:pk>/delete',BlogDeleteApi.as_view()),
]
