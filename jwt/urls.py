from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token



router = DefaultRouter()
router.register('blog', BlogView, basename='blog') # (게시글)
router.register('comment', CommentView, basename='comment') # (댓글)


urlpatterns = [
    path('api/token/',obtain_jwt_token),
    path('api/token/verify/', verify_jwt_token),
    path('api/token/refresh/', refresh_jwt_token),
]