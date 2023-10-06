from django.shortcuts import render

def home(req):
    return render(req,"home.html")

def course(req):
    return render(req,'courses.html')