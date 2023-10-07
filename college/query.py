from course.models import courses
from django.contrib.auth.models import User
from notice.models import notice
from user.models import profile


def select_course(req):
    all_courses = courses.objects.all()
    course_context = {'course':all_courses}
    return course_context


def get_user(req,uid):
    get_user_data = User.objects.get(id = uid)
    user_data = {'data' : get_user_data}
    return user_data

def get_all_notice(req):
    notices = notice.objects.all()
    all_notice = {'data' : notices}
    return all_notice


def get_profile(req,uid):
    prof = profile.objects.get(user_id = uid)
    return prof

def create_user_admin(req,fname,lname,email,username,password,dept):
    try:
        user = User.objects.create_user(first_name = fname,last_name = lname,email= email,password=password,username=username)
    except:
        return False
    prof = profile(dept = dept, profile = 'teacher',user_id=user.id,status ='pending')
    prof.save()
    return True


def create_user_student(req,fname,lname,email,username,password,dept):
    try:
        user = User.objects.create_user(first_name = fname,last_name = lname,email= email,password=password,username=username)
    except:
        return False
    prof = profile(dept = dept, profile = 'student',user_id=user.id,status ='pending')
    prof.save()
    return True