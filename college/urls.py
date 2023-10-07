"""college URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from college import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('courses/',views.course,name='course'),
    path('admin_login/',views.admin_login,name='admin_login'),
    path('admin_post/',views.login_admin_post,name='admin_post'),
    path('admin_panel/<uid>/',views.admin_panel,name='admin'),
    path('admin_logout/',views.admin_log_out,name='admin_logout'),
    path('student_login/',views.student_login,name='student_login'),
    path('student_registration/',views.student_registration,name='student_registration')
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
