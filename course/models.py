from django.db import models

# Create your models here.
class courses(models.Model):
    courses =  models.CharField(max_length=255)

    def __str__(self) -> str:
        return  self.courses
    

class year(models.Model):
    year = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.year
    
class university(models.Model):
    university = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.university
    
class board_ten(models.Model):
    board_ten = models.CharField(max_length=255)


class board_twelve(models.Model):
    board_twelve = models.CharField(max_length=255)
