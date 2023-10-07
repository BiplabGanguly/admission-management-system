from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from college.query import select_course,get_user,get_all_notice,get_profile

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


def login_admin_post(req):
    if req.method == "POST":
        username = req.POST['username']
        userpass = req.POST['password']
      
        user = authenticate(username=username,password=userpass)
        prof = get_profile(req,user.id)

        if user is not None and prof.profile == 'teacher':
            login(req, user)
            return redirect("admin",user.id)
        else:
            return redirect('home')
        

@login_required(login_url='/')
def admin_panel(req,uid):
    context = get_user(req,uid)
    return render(req,'adminpanel.html',context)


@login_required(login_url='/')
def admin_log_out(req):
    logout(req)
    return redirect("admin_login")