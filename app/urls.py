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
]