from django.db import models

# Create your models here.
class courses(models.Model):
    courses =  models.CharField(max_length=255)

    def __str__(self) -> str:
        return  self.courses
