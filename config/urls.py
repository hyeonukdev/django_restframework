from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('account/', include('account.urls')),
    path('student/', include('student.urls')),
    path('blog/', include('blog.urls')),
    path('jwt/', include('blog.urls')),

    path('api/token/',obtain_jwt_token),
    path('api/token/verify/', verify_jwt_token),
    path('api/token/refresh/', refresh_jwt_token),
]