from django.contrib import admin
from course.models import courses
from notice.models import notice
# Register your models here.

admin.site.register(courses)
admin.site.register(notice)
