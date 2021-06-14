from django.urls import path, include
from .views import BlogView, CommentView
from .api import BlogApi, BlogCreateApi, BlogUpdateApi, BlogDeleteApi
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('blog', BlogView, basename='blog') # (게시글)
router.register('comment', CommentView, basename='comment') # (댓글)


urlpatterns = [
    path('api',BlogApi.as_view()),
    path('api/create',BlogCreateApi.as_view()),
    path('api/<int:pk>',BlogUpdateApi.as_view()),
    path('api/<int:pk>/delete',BlogDeleteApi.as_view()),
    path('', include(router.urls)),
]