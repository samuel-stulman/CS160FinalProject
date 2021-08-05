# chat/views.py
from django.shortcuts import render

# Home page
def index(request):
    return render(request, 'index.html')

def loginpage(request):
    return render(request, 'login.html')

def privacy(request):
    return render(request, 'privacy.html')

def aboutpage(request):
    return render(request, 'about.html')

def newblog(request):
    return render(request, 'addblog.html')

def newtask(request):
    return render(request, 'addtask.html')

def feed(request):
    return render(request, 'feed.html')

def profile(request):
    return render(request, 'profile.html')

def settings(request):
    return render(request, 'settings.html')

def todo(request):
    return render(request, 'todo.html')

def help(request):
    return render(request, 'help.html')

def register(request):
    return render(request, 'register.html')