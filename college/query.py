from course.models import courses, university, board_ten, board_twelve,session
from django.contrib.auth.models import User
from notice.models import notice
from user.models import profile, educational_details


def select_course(req):
    try:
        all_courses = courses.objects.all()
        course_context = {'course':all_courses}
        return course_context
    except:
        return False

def get_user(req,uid):
    try:
        get_user_data = User.objects.get(id = uid)
        user_data = {'data' : get_user_data}
        return user_data
    except:
        return False


def get_all_notice(req):
    try:
        notices = notice.objects.all()
        all_notice = {'data' : notices}
        return all_notice
    except:
        return False
    

def add_notice(req,notices,dept):
    try:
        note = notice(notice = notices, dept = dept)
        note.save()
        return True
    except:
        return False

    

def get_all_course_model(req):
    try:
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
    except:
        return False


def get_profile(req,uid):
    try:
        prof = profile.objects.get(user_id = uid)
        return prof
    except:
        return False

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


def get_all_pending_student_data(req,dept):
    try:
        pending_student_data = profile.objects.select_related('user').filter(dept = dept).filter(profile = 'student').filter(status = 'pending')
        return pending_student_data
    except:
        return False


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

def get_all_admin_data(req,dept):
    try:
        all_admin_data = profile.objects.select_related('user').filter(profile = 'admin',status = 'accept', dept = dept)
        return all_admin_data
    except:
        return False


def count_dept(req):
    try:
        count_dept = courses.objects.all().count()
        return count_dept
    except:
        return False


def total_student(req):
    try:
        total_student = educational_details.objects.select_related('user__profile').filter(verify='accept',user__profile__profile='student').count()
        return total_student
    except:
        return False


def total_dept_student(req,dept):
    try:
        total_dept_student = educational_details.objects.select_related('user__profile').filter(verify='accept',user__profile__dept=dept,user__profile__profile='student').count()
        return total_dept_student
    except:
        return False


def add_student_details(req,uid,father_name, mother_name,gender,address,dept,date):
    try:
        profile.objects.filter(user_id = uid).update(fathers_name = father_name,mothers_name = mother_name,
                                                     gender = gender,address = address,dept = dept,birth_date = date )
    except:
        return False
    return True

def add_student_images(req,uid,image):
    try:
        profile.objects.filter(user_id = uid).update(user_img = image)
    except:
        return False
    return True


def upadte_user_details(req,uid,f_name, l_name, email, username):
    try:
        user = User.objects.get(id = uid)
        user.first_name = f_name
        user.last_name = l_name
        user.email = email
        user.username = username
        user.save()
        return True
    except:
        return False



def add_student_education(req,uid,ten_board,ten_percentage,twelve_board,twelve_percentage,university,gpa,session_start,session_end):
    try:
        edu = educational_details(user_id = uid,board_ten = ten_board, percentage_ten = ten_percentage,
                              	board_twelve = twelve_board,percentage_twelve = twelve_percentage,
                                  university = university,cgpa = gpa, s_start = session_start,
                                     s_end = session_end,verify = 'pending')
        edu.save()
    except:
        return False
    return True


def add_ten_result(req,uid,image):
    try:
        educational_details.objects.filter(user_id = uid).update(ten_result = image)
    except:
        return False
    return True

def add_twelve_result(req,uid,image):
    try:
        educational_details.objects.filter(user_id = uid).update(twelve_result = image)
    except:
        return False
    return True


def get_education_submit(req,uid):
    try:
        edu = educational_details.objects.get(user_id = uid)
        return edu
    except: 
        return False

def get_all_verify_student_data(req,dept):
    try:
        pending_student_data = educational_details.objects.select_related('user__profile').filter(verify='pending',user__profile__dept=dept,user__profile__status = 'accept')
        return pending_student_data
    except:
        return False

def accept_verify_student(req,sid):
    try:
        educational_details.objects.filter(user_id = sid).update(verify = 'accept')
        return True
    except:
        return False

def reject_verify_student(req,sid):
    try:
        educational_details.objects.filter(user_id = sid).update(verify = 'reject')
        return True
    except:
        return False


def get_all_dept_student(req,dept):
    try:
        all_student_data = educational_details.objects.select_related('user__profile').filter(verify='accept',user__profile__dept=dept,user__profile__status = 'accept')
        return all_student_data
    except:
        return False
    

def pending_info(req,dept):
    try:
        count_prof = profile.objects.filter(dept = dept, status = 'pending').count()
        return count_prof
    except:
        return False
    
def pending_verify_info(req,dept):
    try:
        count_verify_info = educational_details.objects.select_related('user__profile').filter(verify = 'pending', user__profile__dept = dept).count()
        return count_verify_info
    except:
        return False


