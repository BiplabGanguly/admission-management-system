from django.shortcuts import render,redirect
from notice.models import notice
from user.models import profile
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def home(req):
    data = notice.objects.all()
    dt={}
    dt['data']=data
    return render(req,"home.html",dt)

def course(req):
    return render(req,'courses.html')

def admin_login(req):
    return render(req,'adminlogin.html')


def login_admin_post(req):
    if req.method == "POST":
        username = req.POST['username']
        userpass = req.POST['password']
      
        user = authenticate(username=username,password=userpass)
        prof = profile.objects.get(user_id = user.id)

        if user is not None and prof.profile == 'teacher':
            login(req, user)
            return redirect("admin",user.id)
        else:
            return redirect('home')
        

@login_required(login_url='/')
def admin_panel(req,uid):
    user_data = User.objects.get(id = uid)
    context = {'data' : user_data}
    return render(req,'adminpanel.html',context)


def admin_log_out(req):
    logout(req)
    return redirect("home")