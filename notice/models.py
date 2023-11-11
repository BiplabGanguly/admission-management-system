from django.db import models
from course.models import courses

# Create your models here.
class notice(models.Model):
    dept = models.TextField(max_length=255)
    notice = models.TextField()

    def __str__(self) -> str:
        return self.dept

