from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('index/', views.plot_avg_milk_vm, name='index'),
    path('milking/', views.plot_avg_daily_milk_milking_per_cow, name='milking'),
    path('milkvolact/',views.plot_milking_lact, name='milkvolat')
    #path('top', views.top, name='top'),
]