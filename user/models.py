from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class profile(models.Model):
    status_choice = [('pending', 'pending'),
                     ('accept', 'accept'),
                     ('reject', 'reject'),]
    profile_choice = [('admin', 'admin'),
                      ('student', 'student')]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fathers_name = models.CharField(max_length=255, blank=True)
    mothers_name = models.CharField(max_length=255, blank=True)
    birth_date = models.CharField(max_length=255, blank=True)
    gender = models.CharField(max_length=255, blank=True)
    address = models.TextField(blank=True)
    dept = models.CharField(max_length=255, blank=True)
    user_img = models.FileField(upload_to="", blank=True)
    status = models.CharField(max_length=255, blank=True, choices=status_choice)
    profile = models.CharField(max_length=255, choices=profile_choice)

    def __str__(self) -> str:
        return self.user.first_name


class educational_details(models.Model):
    verify_choice = [('pending', 'pending'),
                     ('accept', 'accept'),
                     ('reject', 'reject'),]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    board_ten = models.CharField(max_length=255, blank=True)
    percentage_ten = models.CharField(max_length=255, blank=True)
    ten_result = models.FileField(upload_to="", blank=True)
    board_twelve = models.CharField(max_length=255, blank=True)
    percentage_twelve = models.CharField(max_length=255, blank=True)
    twelve_result = models.FileField(upload_to="", blank=True)
    university = models.CharField(max_length=255, blank=True)
    cgpa = models.CharField(max_length=255, blank=True)
    s_start = models.CharField(max_length=255, blank=True)
    s_end = models.CharField(max_length=255, blank=True)
    verify = models.CharField(
        max_length=255, default='false', choices=verify_choice)

    def __str__(self) -> str:
        return self.user.first_name
