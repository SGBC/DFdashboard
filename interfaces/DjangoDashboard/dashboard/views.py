from django.contrib.auth.models import User
from django.shortcuts import render
from pyecharts.charts import Bar
from django_echarts.views.backend import EChartsBackendView
from django.contrib import messages
import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd
import operator
# Create your views here.
Path = "G:\\git\\interfaces\\mysite\\keyvalue_testdata\\keyvalues.csv"

def Readfiles(Path):
    csvFile = open(Path, "r")
    reader = csv.reader(csvFile)

    result = []
    
    # read files
    for item in reader:
        if reader.line_num == 1:
            continue
        result.append(item)
    csvFile.close()
    return result


def index(request):
    #load data from csv
    result = np.array(Readfiles(Path))
    Date = list(result[:,0])

    avg_daily_milk_per_cow = list(result[:,1])
    avg_daily_nr_of_milkings_per_cow = list(result[:,2])

    nr_of_milkings_cows_yesterday = list(result[:,3])

    v1 = list(result[:,4])
    v2 = list(result[:,5])
    vm_all = list(result[:,6])

    avg_nr_pass_smartgate = list(result[:,7])
    avg_nr_of_kickoffs = list(result[:,9])
    milk_to_tank_yesterday = list(result[:,11])

    time_in_robot = list(result[:,10])

    avg_lact_0_100 = list(result[:,15])
    avg_lact_101_200 = list(result[:,16])
    avg_lact_201 = list(result[:,17])

    # return values to dashboard
    return render(request,"dashboard.html",
        {
            'Date':Date,
            'avg_per_cow':avg_daily_milk_per_cow, 'avg_nr_milking_per_cow': avg_daily_nr_of_milkings_per_cow,
            'vm1':v1, 'vm2':v2, 'vm_all':vm_all,
            'smartgate':avg_nr_pass_smartgate, 'kickoffs':avg_nr_of_kickoffs, 'milk_yesterday': milk_to_tank_yesterday,
            'time_in_robot':time_in_robot,
            'lact_0_100':avg_lact_0_100, 'lact_101_200':avg_lact_101_200, 'lact_201':avg_lact_201
        }
    )


def login(request):
    return render(request, "Login.html")

def alertMessege(request):
    return 