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
    path('admin_post_login/',views.login_admin_post,name='admin_post_login'),
    path('admin_panel/<uid>/',views.admin_panel,name='admin'),
    path('admin_logout/',views.admin_log_out,name='admin_logout'),
    path('student_login/',views.student_login,name='student_login'),
    path('student_registration/',views.student_registration,name='student_registration'),
    path('admin_ragistration',views.admin_registration,name='admin_ragistration'),
    path('admin_post_ragistration/',views.admin_post_ragistration,name='admin_post_ragistration'),
    path('status/<uid>/',views.status_page,name='status_page'),
    path('student_ragistration_post',views.student_post_ragistration,name='student_post_ragistration'),
    path('student_panel/<sid>/',views.student_panel,name='student_panel'),
    path('login_student_post/',views.login_student_post,name='login_student_post'),
    path('accept_student/<sid>/',views.accept_student,name='accept_student'),
    path('reject_student/<sid>/',views.reject_student,name='reject_student'),
    path('pending_student/<uid>/',views.pending_student,name='pending_student'),
    path('add_student_data/<uid>/',views.add_student_data,name="add_student_data"),
    path('pending_student_verification/<uid>/',views.pending_student_verification,name="pending_student_verification"),
    path('all_student_details/<sid>/',views.all_student_details,name="all_student_details"),
    path('accept_verify_student/<sid>/',views.accept_verify_student,name = "accept_verify_student"),
    path('reject_verify_student/<sid>/',views.reject_verify_student,name = 'reject_verify_student'),
    path('all_stuent_list/<uid>/',views.all_stuent_list,name = "all_stuent_list"),
    path('block_student/<sid>/',views.block_student,name = 'block_student'),
    path('accept/<sid>/',views.admission_complete,name = "accept"),
    path('add_notice/<uid>/',views.addnotice,name = "add_notice"),
    path('publish_notice/<uid>/',views.publish_notice,name='publish_notice'),
    path('notice/',views.article,name='notice'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

