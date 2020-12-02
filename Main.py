import pandas as pd

import functions as func

files=[]
for i in range(14):
    if i<8:
        files.append("extractions/extraction_DelPro-5.3_2020110{}_03-10/GIGACOW_milkings_v2_2020110{}.csv".format(i+2, i+2))
    else:
        files.append("extractions/extraction_DelPro-5.3_202011{}_03-10/GIGACOW_milkings_v2_202011{}.csv".format(i+2, i+2))

data = pd.concat((pd.read_csv(filename, sep = ';', decimal=',', header = 1) for filename in files), ignore_index = True)

data2 = pd.read_csv("extractions/extraction_DelPro-5.3_20201116_03-10/GIGACOW_feed_v1_20201116 001002.csv", encoding='latin-1')
data3 = pd.read_csv("extractions/extraction_DelPro-5.3_20201116_03-10/GIGACOW_identity_v1_20201116 002000.csv")

data=func.preprocess_milkings(data)

print('Average 7 days, nr of kickOffs: ', func.avg_kickOffs(data['Date'], data['Nr_of_kickOffs']))
print('Average 7 days, time in robot: ', func.avg_time_in_robot(data['Milk_duration']))

print('Average 7 days, milking Volym. ', func.num_day_lactation_0_100(data2['Days In Milk']), ' cows in lactation 0-100: ', func.avg_milking_volume_lact_0_100(data['Date'], data['Animal_ID'], data['Action'], data['Milk_yield'], data3['Animal Number'], data3['Official Reg. No. (ORN)'], data2['Official Reg. No. (ORN)'], data2['Days In Milk']))
print('Average 7 days, milking Volym. ', func.num_day_lactation_101_200(data2['Days In Milk']), ' cows in lactation 101-200: ', func.avg_milking_volume_lact_101_200(data['Date'], data['Animal_ID'], data['Action'], data['Milk_yield'], data3['Animal Number'], data3['Official Reg. No. (ORN)'], data2['Official Reg. No. (ORN)'], data2['Days In Milk']))
print('Average 7 days, milking Volym. ', func.num_day_lactation_201_up(data2['Days In Milk']), ' cows in lactation 200-: ', func.avg_milking_volume_lact_201_up(data['Date'], data['Animal_ID'], data['Action'], data['Milk_yield'], data3['Animal Number'], data3['Official Reg. No. (ORN)'], data2['Official Reg. No. (ORN)'], data2['Days In Milk']))

stat = func.cow_stat(data['Date'], data['Animal_ID'], data['Milk_duration'], data['Action'], data['Milk_yield'], data['Nr_of_kickOffs'], data3['Animal Number'], data3['Official Reg. No. (ORN)'], data2['Official Reg. No. (ORN)'], data2['Days In Milk'])

print(stat)
print(stat[stat['Nr_of_kickOffs']>2])

#data.to_csv("testdata.csv",index=False)
