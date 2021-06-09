from django.urls import path, include
from . import views
from rest_framework import urls

urlpatterns =[
    path('', views.UserList.as_view()),
    path('signup/', views.UserCreate.as_view()),
    path('<int:pk>/', views.UserUpdate.as_view()),
    path('<int:pk>/delete/', views.UserDelete.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='account')),
    path('super/', views.SuperUserList.as_view()),
    path('super/signup/', views.SuperUserCreate.as_view()),
    path('super/<int:pk>/', views.SuperUserUpdate.as_view()),
    path('super/<int:pk>/delete', views.SuperUserDelete.as_view()),
 ]