from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from user import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('employee/', include('employee.urls')),
    path('user/', include('user.urls')),
]