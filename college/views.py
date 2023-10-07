from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from college.query import select_course,get_user,get_all_notice,get_profile,create_user

def home(req):
    dt = get_all_notice(req)
    return render(req,"home.html",dt)

def course(req):
    return render(req,'courses.html')

def admin_login(req):
    return render(req,'adminlogin.html')

def student_login(req):
    return render(req,'studentlogin.html')

def student_registration(req):
    data = select_course(req)
    return render(req,'studentregistration.html',data)

def admin_registration(req):
    data = select_course(req)
    return render(req,'adminragistration.html',data)

def status_page(req):
    return render(req,'status.html')


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
            create_user(req,f_name,l_name,email,username,ps,dept)
            return redirect('admin_login')
        else:
            return redirect('admin_ragistration')


def login_admin_post(req):
    if req.method == "POST":
        username = req.POST['username']
        userpass = req.POST['password']

        user = authenticate(username=username,password=userpass)

        if user is not None:
            prof = get_profile(req,user.id)
            if prof.profile == 'teacher' and prof.status == 'accept':
                login(req, user)
                return redirect("admin",user.id)
            elif prof.status == 'pending':
                return redirect('status_page')
            elif prof.status == 'reject':
                return redirect('home')
        else:
            return redirect('home')
        

@login_required(login_url='/')
def admin_panel(req,uid):
    user_data = get_user(req,uid)
    prof_data  = get_profile(req,uid)
    context = {'user_data' : user_data, 'prof_data' : prof_data}
    return render(req,'adminpanel.html',context)


@login_required(login_url='/')
def admin_log_out(req):
    logout(req)
    return redirect("admin_login")