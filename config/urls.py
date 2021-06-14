from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('account/', include('account.urls')),
    path('student/', include('student.urls')),
    path('blog/', include('blog.urls')),
    path('jwt/', include('blog.urls')),
]