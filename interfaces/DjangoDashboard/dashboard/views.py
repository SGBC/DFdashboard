from django.contrib.auth.models import User
from django.shortcuts import render
from django_echarts.views.backend import EChartsBackendView
from django.contrib import messages
import numpy as np
import csv
import os
import pandas as pd
import operator
import time
 
# Create your views here.
Path = "..\\..\\keyvalue_testdata"   # path to the keyvalues folder

def Readfiles(filename, flag):
    csvFile = open(filename, "r")
    reader = csv.reader(csvFile)

    result = []
    
    # read files
    for item in reader:
        if reader.line_num == 1 and flag == 0:
            continue
        result.append(item)
    csvFile.close()

    return result

# load todo list --> index.html
def todolist_load():
    data = Readfiles('todo_list.csv', 0)
    '''
    # load excel 
    List= xlrd.open_workbook('todo_list.xlsx')
    rows = List.get_rows()
    table =[]
    for row in rows:
        table.append(row.value)
        '''
    data = np.array(data)
    #print(len(data))
    now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    #print(now)
    List = []
    if (len(data) != 0):
        for activity in data:
            time_start = activity[1] + ' ' + activity[2]
            time_end = activity[1] +  ' ' +activity[3]
            status = 0      # flag for status, 0 for not started, 1 for ongoing, 2 for complete
            if (time_start > now):
                status = 0
            elif (time_start <= now) and (now <= time_end):
                status = 1
            else :
                status = 2
            event = [activity[0], status]
            List.append(event)
            #print(time_start, time_end)   
    
    return List  

def index(request):
    #load data from csv
    keyvalues = "keyvalues.csv"
    result = np.array(Readfiles(Path + "\\" + keyvalues, 0))
    
    if os.path.exists('todo_list.csv'):  # if exists, load file
        List = todolist_load()
    else: 
        List = []
      
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

    # lactaion
    avg_lact_0_100 = np.mean(list(map(float, result[:,15])))
    avg_lact_101_200 = np.mean(list(map(float, result[:,16])))
    avg_lact_201 = np.mean(list(map(float, result[:,17])))

    # bad economy cows
    # load files kickOffs, stat_milking_more_below_thre, stat_milking_once...
    kickOffs = "kickOffs.csv"
    milking_more = "stat_milking_more_below_thresh.csv"
    milking_once = "stat_milking_once_below_thresh.csv"
    kickOffs_ID = []
    milking_more_ID = []
    milking_once_ID = []
    # load animal ID
    loadfile = np.array(Readfiles(Path + "\\" + kickOffs, 0))
    #print(len(loadfile))
    if (len(loadfile) != 0):
        kickOffs_ID =list(map(int,loadfile[:,1]))
        
    loadfile = np.array(Readfiles(Path + "\\" + milking_more, 0))
    #print(len(loadfile))
    if (len(loadfile) != 0):
        milking_more_ID = list(map(int,loadfile[:,1]))
        
    loadfile = np.array(Readfiles(Path + "\\" + milking_once, 0))
    #print(len(loadfile))
    if (len(loadfile) != 0):
        milking_once_ID = list(map(int,loadfile[:,1]))

    '''
    animal_ID = np.empty((Len, 3))
    print(len(animal_ID))
    animal_ID[:,0] = kickOffs_ID
    animal_ID[:,1] = milking_more_ID
    animal_ID[:,2] = milking_once_ID
    #print(Len, len(milking_more_ID), len(kickOffs_ID), len(milking_once_ID))
    #animal_ID = pd.DataFrame({'kickOffs': kickOffs_ID, 'milking_more': milking_more_ID})
    '''

    #merge into a tabel
    animal_ID = {'kickOffs': kickOffs_ID, 'milking_more': milking_more_ID, 'milking_once': milking_once_ID}
    ID = list(animal_ID.values())
    #print(ID)
    # return values to dashboard
    return render(request,"dashboard.html",
        {
            'Date':Date,
            'avg_per_cow':avg_daily_milk_per_cow, 'avg_nr_milking_per_cow': avg_daily_nr_of_milkings_per_cow,
            'vm1':v1, 'vm2':v2, 'vm_all':vm_all,
            'smartgate':avg_nr_pass_smartgate, 'kickoffs':avg_nr_of_kickoffs, 'milk_yesterday': milk_to_tank_yesterday,
            'time_in_robot':time_in_robot,
            'lact_0_100':round(avg_lact_0_100,2), 'lact_101_200':round(avg_lact_101_200,2), 'lact_201':round(avg_lact_201,2),
            'kick_ID': kickOffs_ID, 'milking_more':milking_more_ID,
            'todo': List, 'animal_ID': animal_ID,

        }
    )

# login 
def login(request):
    return render(request, "Login.html")


# pop-up calendar, page for adding events
def calendar(request):
    
    return render(request, "calendar.html")


# write activities into local file
Title = []
begin = []
Date = []
end = []
Description = []

def todolist_write(request):
    if request.method == 'POST':   # get values from front end
        Title.append(request.POST.get('title'))
        Date.append(request.POST.get('day'))
        begin.append(request.POST.get('c1'))
        end.append(request.POST.get('c2'))
        Description.append(request.POST.get('Description'))
    #print(Title, begin, end, Description)
    # write into csv file (title, time begin, time end, description)
    dataframe = pd.DataFrame({'Title': Title, 'Date': Date, 'Time begin': begin, 'Time end': end, 'Description': Description})
    dataframe.to_csv("todo_list.csv", index=False, sep=',')
    '''
    # here is the method if you try to write in file into excel
    workbook =xlsxwriter.Workbook('todo_list.xlsx')
    worksheet = workbook.add_worksheet('todo')
    heading = ['Title', 'Begin', 'End', 'Description']
    worksheet.write_row('A1',heading)
    worksheet.write_column('A2',Title)
    worksheet.write_column('B2',begin)
    worksheet.write_column('C2',end)
    worksheet.write_column('D2',Description)
    
    workbook.close()
    '''
    return render(request,'calendar.html')

               

# example pop-up window for cow informations
def detail(request):
    csvFile = open("..\\..\\extractions\\extraction_DelPro-5.3_20201107_03-10\\GIGACOW_identity.csv", "r")
    reader = csv.reader(csvFile)
    detail_data = []

    for item in reader:
        detail_data.append(item)
        detail_data.append("\n")

    return render (request, "details.html",{'details': detail_data})
