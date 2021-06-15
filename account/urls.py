from django.urls import path, include
from . import views
from rest_framework import urls

urlpatterns =[
    path('api/', views.UserList.as_view()),
    path('api/signup/', views.UserCreate.as_view()),
    path('api/<int:pk>/', views.UserUpdate.as_view()),
    path('api/<int:pk>/delete/', views.UserDelete.as_view()),

    path('api/super/', views.SuperUserList.as_view()),
    path('api/super/signup/', views.SuperUserCreate.as_view()),
    path('api/super/<int:pk>/', views.SuperUserUpdate.as_view()),
    path('api/super/<int:pk>/delete/', views.SuperUserDelete.as_view()),

    path('api/api-auth/', include('rest_framework.urls', namespace='account')),
 ]
