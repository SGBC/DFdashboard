from django.urls import path
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('login/',views.login, name='login'),
    path('detail/', views.detail, name='detail'),
    path('calendar/', views.calendar, name='calendar'),
    path('todo/', views.todolist_write, name='todolist_write')
]