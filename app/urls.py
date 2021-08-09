# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.loginpage, name='login'),
    path('about', views.aboutpage, name='about'),
    path('newblog', views.newblog, name='new blog'),
    path('newtask', views.newtask, name='new task'),
    path('feed', views.feed, name='feed'),
    path('help', views.help, name='help'),
    path('privacy', views.privacy, name='privacy'),
    path('settings', views.settings, name='settings'),
    path('profile', views.profile, name='profile'),
    path('todo', views.todo, name='todo'),
    path('register1', views.register1, name='register1'),
    path('register2', views.register2, name='register2'),
    path('register3', views.register3, name='register3'),
    path('register4', views.register4, name='register4'),
    path('chat', views.chat, name='chat'),
    path('task', views.task, name='task'),
    path('blog', views.blog, name='blog'),
    path('recommend', views.recommendeduser, name='recommended users')
]
