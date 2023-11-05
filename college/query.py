from course.models import courses, university, board_ten, board_twelve,session
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

def get_all_course_model(req):
    universitys = university.objects.all()
    boardten = board_ten.objects.all()
    boardtwelve = board_twelve.objects.all()
    sess = session.objects.all()
    data = {'universitys' :universitys,
            'boardten' : boardten,
            'boardtwelve' : boardtwelve,
            'year' : sess
             }
    return data


def get_profile(req,uid):
    prof = profile.objects.get(user_id = uid)
    return prof

def create_user_admin(req,fname,lname,email,username,password,dept):
    try:
        user = User.objects.create_user(first_name = fname,last_name = lname,email= email,password=password,username=username)
    except:
        return False
    prof = profile(dept = dept, profile = 'admin',user_id=user.id,status ='pending')
    prof.save()
    return True


def create_user_student(req,fname,lname,email,username,password,dept,gender):
    try:
        user = User.objects.create_user(first_name = fname,last_name = lname,email= email,password=password,username=username)
    except:
        return False
    prof = profile(dept = dept, profile = 'student',user_id=user.id,status ='pending',gender = gender)
    prof.save()
    return True


def get_all_pending_student_dada(req,dept):
    pending_student_data = profile.objects.select_related('user').filter(dept = dept).filter(profile = 'student').filter(status = 'pending')
    return pending_student_data


def update_student_accept(req,sid):
    try:
        profile.objects.filter(user_id = sid).update(status = 'accept')
    except:
        return False
    return True


def update_student_reject(req,sid):
    try:
        profile.objects.filter(user_id = sid).update(status = 'reject')
    except:
        return False
    return True

def get_all_admin_data(req):
    all_admin_data = profile.objects.select_related('user').filter(profile = 'admin').filter(status = 'accept')
    return all_admin_data


def count_dept(req):
    count_dept = courses.objects.all().count()
    return count_dept


def total_student(req):
    total_student = profile.objects.select_related('user').filter(profile = 'student').filter(status = 'accept').count()
    return total_student


def total_dept_student(req,dept):
    total_dept_student = profile.objects.select_related('user').filter(dept = dept).filter(profile = 'student').filter(status = 'accept').count()
    return total_dept_student


def add_student_details(req,uid,father_name, mother_name,gender,address,dept,date):
    profile.objects.filter(user_id = uid).update(fathers_name = father_name, 
                                                 mothers_name = mother_name,
                                                  gender = gender,
                                                   address = address,
                                                    dept = dept,
                                                     birth_date = date )
    return True

def add_student_images(req,uid,image):
    profile.objects.filter(user_id = uid).update(user_img = image)
    return True