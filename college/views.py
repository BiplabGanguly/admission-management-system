from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from college.query import get_profile
from college import query

def home(req):
    dt = query.get_all_notice(req)
    return render(req,"home.html",dt)

def course(req):
    return render(req,'courses.html')

def admin_login(req):
    return render(req,'adminlogin.html')

def student_login(req):
    return render(req,'studentlogin.html')

def student_registration(req):
    data = query.select_course(req)
    return render(req,'studentregistration.html',data)

def admin_registration(req):
    data = query.select_course(req)
    return render(req,'adminragistration.html',data)

def admin_post_ragistration(req):
    if req.method == "POST":
        f_name = req.POST['f_name']
        l_name = req.POST['l_name']
        email = req.POST['email']
        dept = req.POST['dept']
        username = req.POST['username']
        ps = req.POST['password']
        c_pass = req.POST['c_password']
        if ps == c_pass:
            result = query.create_user_admin(req,f_name,l_name,email,username,ps,dept)
            if result == True:
                return redirect('admin_login')
            else:
                return redirect('admin_ragistration')
        else:
            return redirect('admin_ragistration')


def login_admin_post(req):
    if req.method == "POST":
        username = req.POST['username']
        userpass = req.POST['password']
        user = authenticate(username=username,password=userpass)  
        if user is not None:
            prof = get_profile(req,user.id)
            if prof.profile == 'admin' and prof.status == 'accept':
                login(req, user)
                return redirect("admin",user.id)
            elif prof.status == 'pending':
                login(req, user)
                return redirect('status_page',user.id)
            elif prof.status == 'reject':
                return redirect('home')
        else:
            return redirect('home')
        

def student_post_ragistration(req):
    if req.method == "POST":
        f_name = req.POST['f_name']
        l_name = req.POST['l_name']
        email = req.POST['email']
        dept = req.POST['dept']
        gender = req.POST['gender']
        username = req.POST['username']
        ps = req.POST['pword']
        c_pass = req.POST['c_pword']
        if ps == c_pass:
            result = query.create_user_student(req,f_name,l_name,email,username,ps,dept,gender)
            if result == True:
                return redirect('student_login')
            else:
                return redirect('student_registration')
        else:
            return redirect('student_registration')


def login_student_post(req):
    if req.method == "POST":
        username = req.POST['username']
        userpass = req.POST['password']
        user = authenticate(username=username,password=userpass)  
        if user is not None:
            prof = get_profile(req,user.id)
            if prof.profile == 'student' and prof.status == 'accept':
                login(req, user)
                return redirect("student_panel",user.id)
            elif prof.status == 'pending':
                login(req, user)
                return redirect('status_page',user.id)
            elif prof.status == 'reject':
                return redirect('home')
        else:
            return redirect('home')


# login required.......................................................

@login_required(login_url='/') 
def admin_panel(req,uid):
    req.session['uid']= uid
    # query
    user_data = query.get_user(req,uid)
    prof_data  = get_profile(req,uid)
    all_admin = query.get_all_admin_data(req)
    count_dept = query.count_dept(req)
    total_student = query.total_student(req)
    total_dept_student = query.total_dept_student(req,prof_data.dept)

    # dict
    context = {'user_data' : user_data, 'prof_data' : prof_data,'all_admin':all_admin}
    context['count_dept'] = count_dept
    context['total_student'] = total_student
    context['total_dept_student'] = total_dept_student
    return render(req,'adminpanel.html',context)


@login_required(login_url='/')
def status_page(req,uid):
    user_data = query.get_user(req,uid)
    return render(req,'status.html',user_data)

@login_required(login_url='/')
def admin_log_out(req):
    logout(req)
    return redirect("home")

@login_required(login_url='/')
def student_panel(req,sid):
    user_data = query.get_user(req,sid)
    prof_data  = get_profile(req,sid)
    data = query.get_all_course_model(req)
    context = {'user_data' : user_data, 'prof_data' : prof_data, 'data' : data}
    return render(req,'StudentPanel.html',context)

@login_required(login_url='/')
def accept_student(req,sid):
    uid = req.session['uid']
    result = query.update_student_accept(req,sid)
    if result == True:
        return redirect('pending_student',uid)
    else:
        return redirect('admin',uid)
    
@login_required(login_url='/')
def reject_student(req,sid):
    uid = req.session['uid']
    result = query.update_student_reject(req,sid)
    if result == True:
        return redirect('pending_student',uid)
    else:
        return redirect('admin',uid)
    

@login_required(login_url='/')
def pending_student(req,uid):
    req.session['uid']= uid
    # Query
    user_data = query.get_user(req,uid)
    prof_data  = get_profile(req,uid)
    pending_data = query.get_all_pending_student_dada(req,prof_data.dept)
    # dict
    pending_context = {'uid' : uid}
    pending_context['user_data'] = user_data
    pending_context['prof_data'] = prof_data
    pending_context['pending_data'] = pending_data
    return render(req,'PendingStudent.html',pending_context)
