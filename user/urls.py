from django.urls import include, path
from .serializers import UserSerializer, GroupSerializer
from user import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('api/',include(router.urls)),
]
