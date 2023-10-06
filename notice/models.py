from django.db import models
from course.models import courses

# Create your models here.
class notice(models.Model):
    dept = models.ForeignKey(courses, on_delete=models.CASCADE)
    notice = models.TextField()
