from django.urls import include, path
from user import views
from rest_framework import routers
from rest_framework import urls
from .serializers import UserSerializer, GroupSerializer


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('api/',include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='user')),
]
