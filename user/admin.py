from django.contrib import admin
from course.models import courses,year,university,board_ten,board_twelve
from notice.models import notice
from user.models import profile,educational_details
# Register your models here.

admin.site.register(courses)
admin.site.register(notice)
admin.site.register(year)
admin.site.register(university)
admin.site.register(board_ten)
admin.site.register(board_twelve)
admin.site.register(profile)
admin.site.register(educational_details)
