from django.shortcuts import render
from django.http import HttpResponse
import pyecharts as pye
from pyecharts.charts import Bar, Line
import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd
import operator
import pyecharts.options as opt

#result = []
Path = "keyvalues.csv"
# Create your views here.
def Readfiles(Path):
    csvFile = open(Path, "r")
    reader = csv.reader(csvFile)

    result = []
    '''
    avg_nr_of_kick = []
    avg_time_in_robot = []
    vg_milking_volume_lact = []
    cow_in_lac = []
    
    '''
    # load data
    for item in reader:
        if reader.line_num == 1:
            continue
        result.append(item)
    csvFile.close()
    return result#Date, avg_milk_vm_1, avg_milk_vm_2, avg_milk_all#, avg_time_in_robot, avg_nr_of_kick

def index(request):
    return render(request, 'Index.html')

def plot_avg_milk_vm(request):
    Date = []
    avg_milk_vm_1 = []
    avg_milk_vm_2 = []
    avg_milk_all = []
    result = Readfiles(Path)

    for item in result:
        Date.append(item[0])
        # plot3
        avg_milk_vm_1.append(item[4])
        avg_milk_vm_2.append(item[5])
        avg_milk_all.append(item[6])

    attr = Date
    v1 = avg_milk_vm_1
    v2 = avg_milk_vm_2
    bar=(
        Bar()
        .add_xaxis(attr)
        .add_yaxis("avg_milk_vm_1",v1,stack=True, label_opts=False, color='#EE8F71')
        .add_yaxis("avg_milk_vm_2",v2,stack=True,label_opts=False, color='#82C0E9')

    )
    #bar.render()
    line = (
        Line()
        .add_xaxis(attr)
        .add_yaxis('avg milk from vms-1 and 2', avg_milk_all, itemstyle_opts=opt.ItemStyleOpts(
            border_color='#D7D29E'
        ),
                linestyle_opts=opt.LineStyleOpts(width=4, color='#1A476F'),
                   z_level=10)

    )
    # bar  bar.render_embed()
    return HttpResponse(bar.overlap(line).render_embed())

def plot_avg_daily_milk_milking_per_cow(request):
    Date = []
    avg_daily_milk_per_cow = []
    avg_daily_nr_of_milkings_per_cow = []
    result = Readfiles(Path)
    for item in result:
        Date.append(item[0])
        avg_daily_milk_per_cow.append(item[1])
        avg_daily_nr_of_milkings_per_cow.append(item[2])

    line_milk_per_cow = (
        Line()
        .add_xaxis(Date)
        .add_yaxis('avg daily milk per cow',avg_daily_milk_per_cow, linestyle_opts=opt.LineStyleOpts(width=3))
        .add_yaxis('avg daily nr of milkings per cow',avg_daily_nr_of_milkings_per_cow, linestyle_opts=opt.LineStyleOpts(width=3))
        .set_global_opts(
                yaxis_opts=opt.AxisOpts(min_='datamin'),
        )
    )
    return HttpResponse(line_milk_per_cow.render_embed())

def plot_milking_lact(request):
    Date = []
    avg_milking_volume_lact_0_100 = []
    avg_milking_volume_lact_101_200 =[]
    avg_milking_volume_lact_200_ =[]
    lact_0_100 =[]
    lact_101_200 = []
    lact_200 = []
    result = Readfiles(Path)

    for item in result:
        Date.append(item[0])
        lact_0_100.append(item[12])
        lact_101_200.append(item[13])
        lact_200.append(item[14])
        avg_milking_volume_lact_0_100.append(item[15])
        avg_milking_volume_lact_101_200.append(item[16])
        avg_milking_volume_lact_200_.append(item[17])

    bar=(
        Bar()
        .add_xaxis(Date)
        .add_yaxis('0-100',avg_milking_volume_lact_0_100, stack=True, z_level=20, color='#D3D3D3',yaxis_index=0)
        .add_yaxis('101-200', avg_milking_volume_lact_101_200, stack=True, z_level=10, color='#FFFAF0', yaxis_index=0)
        .add_yaxis('200-', avg_milking_volume_lact_200_, stack=True, color="#FFA07A", yaxis_index=0)
        .extend_axis(yaxis=opt.AxisOpts())
        .set_global_opts(
            xaxis_opts=(
                opt.AxisOpts(
                    name='Date',
                    name_location='middle',
                    name_gap=40,
                    name_textstyle_opts=opt.TextStyleOpts(
                        font_family='Time New Roman',
                        font_size=14
                    )
                )
            ),
            yaxis_opts=(
                opt.AxisOpts(
                    name='Milking volume',
                    name_location='middle',
                    name_gap=40,
                    name_textstyle_opts=opt.TextStyleOpts(
                    font_family='Time New Roman',
                    font_size=14
                  )
                )
            )
        )

    )
    line=(
        Line()
        .add_xaxis(Date)
        .add_yaxis('lactation day 0-100', lact_0_100, z_level=40,label_opts=False, yaxis_index=1)
        .add_yaxis('lactation day 101-200', lact_101_200, z_level=40, label_opts=False, yaxis_index=1)
        .add_yaxis('lactation day 200-', lact_200, z_level=40, label_opts=False, yaxis_index=1)
        .set_global_opts(
            yaxis_opts=(
                opt.AxisOpts(name='Lactation Day')
            )
        )
    )
    return HttpResponse(bar.overlap(line).render_embed())