import pandas as pd
import glob

import functions as func

d=7

out_data = pd.DataFrame(columns = ['Date','avg_daily_milk_per_cow', 'avg_daily_nr_of_milkings_per_cow',
    'nr_of_milkings_cows_yesterday', 'avg_milk_from_vms_1', 'avg_milk_from_vms_2', 'avg_milk_from_vms_1_and_2',
    'avg_nr_pass_smartgate', 'projected_monthly_milk', 'avg_nr_of_kickOffs', 'avg_time_in_robot',
    'Milk_to_tank_yesterday', 'cows_lactation_day_0-100', 'cows_lactation_day_101-200', 'cows_lactation_day_201-',
    'avg_milking_volume_lact_0-100', 'avg_milking_volume_lact_101-200', 'avg_milking_volume_lact_201-'])

for of in range(9):
    files = []
    files2 = []
    for i in range(d):
        if (i+of)<8:
            files.append(glob.glob("extractions/extraction_DelPro-5.3_2020110{}_03-10/GIGACOW_milkings*.csv".format(i+2+of))[0])
            files2.append(glob.glob("extractions/extraction_DelPro-5.3_2020110{}_03-10/Cow Traffic*.csv".format(i+2+of))[0])
        else:
            files.append(glob.glob("extractions/extraction_DelPro-5.3_202011{}_03-10/GIGACOW_milkings*.csv".format(i+2+of))[0])
            files2.append(glob.glob("extractions/extraction_DelPro-5.3_202011{}_03-10/Cow Traffic*.csv".format(i+2+of))[0])

    data = pd.concat((pd.read_csv(filename, sep = ';', decimal=',', header = 1) for filename in files), ignore_index = True)

    if (of+d)<9:
        data2 = pd.read_csv(glob.glob("extractions/extraction_DelPro-5.3_2020110{}_03-10/GIGACOW_feed*.csv".format(d+1+of))[0], encoding='latin-1')
        data3 = pd.read_csv(glob.glob("extractions/extraction_DelPro-5.3_2020110{}_03-10/GIGACOW_identity*.csv".format(d+1+of))[0])
    else:
        data2 = pd.read_csv(glob.glob("extractions/extraction_DelPro-5.3_202011{}_03-10/GIGACOW_feed*.csv".format(d+1+of))[0], encoding='latin-1')
        data3 = pd.read_csv(glob.glob("extractions/extraction_DelPro-5.3_202011{}_03-10/GIGACOW_identity*.csv".format(d+1+of))[0])

    dataA2 = pd.concat((pd.read_csv(filename, sep = ',', encoding='latin-1') for filename in files2), ignore_index = True)

    data = func.preprocess_milkings(data)
    dataA2 = func.preprocess_traffic(dataA2)

    #data = pd.concat([data['Date'], data['Animal_ID'], data['Group'], data['Robot'], data['Action'], data['Milk_duration'], data['Milk_yield'], data['Nr_of_milkings'], data['Nr_of_kickOffs'], data['Milk_destination']], axis = 1)
    #dataA2 = pd.concat([dataA2['Animal_ID'], dataA2['Group'], dataA2['Date'], dataA2['Result']], axis = 1)
    #dataA2.to_csv("dataA2.csv", index=False, sep = ';')
    #data.to_csv("data.csv", index=False, sep = ';')

    #print(data)
    #print(dataA2)

    data_cow = func.daily_milk_per_cow(data['Date'], data['Animal_ID'], data['Action'], data['Milk_yield'])

    #data_cow.to_csv("data_cow.csv", index=False, sep = ';')

    v = data['Date'].iloc[-1]

    #"avg_daily_milk_per_cow"
    w1 = func.avg_daily_milk_per_cow(data_cow['Total_milk_yield'])

    #"avg_daily_nr_of_milkings_per_cow"
    w2 = func.avg_nr_of_milkings_per_cow(data_cow['Nr_of_milkings'])

    #"nr_of_milkings_cows_yesterday"
    w3 = func.nr_of_milking_cows_yesterday(data_cow['Date'], data_cow['Total_milk_yield'])

    milk_from_robot = func.avg_milk_from_robots(data['Date'], data['Robot'], data['Action'], data['Milk_yield'])
    #"avg_milk_from_vms_1"
    w4 = milk_from_robot[1]
    #"avg_milk_from_vms_2"
    w5 = milk_from_robot[3]
    #"avg_milk_from_vms_1_and_2"
    w6 = milk_from_robot[-1]


    #"avg_nr_pass_smartgate"
    w7 = func.avg_nr_pass_smartgate(dataA2['Animal_ID'], dataA2['Date'], dataA2['Result'])

    #projected_monthly_milk
    w8 = func.proj_monthly_milk(milk_from_robot)

    v1 = func.avg_kickOffs(data['Date'], data['Animal_ID'], data['Nr_of_kickOffs'])
    v2 = func.avg_time_in_robot(data['Milk_duration'])
    v3 = func.milk_to_tank_yesterday(data['Date'], data['Milk_yield'], data['Milk_destination'])
    v4 = func.num_day_lactation_0_100(data2['Days In Milk'])
    v5 = func.num_day_lactation_101_200(data2['Days In Milk'])
    v6 = func.num_day_lactation_201_up(data['Animal_ID'], data['Milk_yield'], data3['Animal Number'], data3['Official Reg. No. (ORN)'], data2['Official Reg. No. (ORN)'], data2['Days In Milk'])


    v7 = func.avg_milking_volume_lact_0_100(data['Date'], data['Animal_ID'], data['Action'], data['Milk_yield'], data3['Animal Number'], data3['Official Reg. No. (ORN)'], data2['Official Reg. No. (ORN)'], data2['Days In Milk'])
    v8 = func.avg_milking_volume_lact_101_200(data['Date'], data['Animal_ID'], data['Action'], data['Milk_yield'], data3['Animal Number'], data3['Official Reg. No. (ORN)'], data2['Official Reg. No. (ORN)'], data2['Days In Milk'])
    v9 = func.avg_milking_volume_lact_201_up(data['Date'], data['Animal_ID'], data['Action'], data['Milk_yield'], data3['Animal Number'], data3['Official Reg. No. (ORN)'], data2['Official Reg. No. (ORN)'], data2['Days In Milk'])

    out_data = out_data.append({'Date': v, 'avg_daily_milk_per_cow': w1, 'avg_daily_nr_of_milkings_per_cow': w2, 
        'nr_of_milkings_cows_yesterday': w3, 'avg_milk_from_vms_1': w4, 'avg_milk_from_vms_2': w5,
        'avg_milk_from_vms_1_and_2': w6, 'avg_nr_pass_smartgate': w7, 'projected_monthly_milk': w8,
        'avg_nr_of_kickOffs': v1,'avg_time_in_robot': v2,'Milk_to_tank_yesterday': v3,'cows_lactation_day_0-100': v4,
        'cows_lactation_day_101-200': v5,'cows_lactation_day_201-': v6,'avg_milking_volume_lact_0-100': v7,
        'avg_milking_volume_lact_101-200': v8, 'avg_milking_volume_lact_201-': v9},
        ignore_index = True)

out_data.to_csv("keyvalues.csv", index=False)
#out_data.to_csv("keyvaluesOverView.csv", index=False, sep = ';')
