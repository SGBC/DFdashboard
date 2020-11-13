import pandas as pd
from functions_Bjorn import avg_kickOffs
from functions_Bjorn import avg_in_robot
from functions_Bjorn import milk_to_tank_today

from functions_Bjorn import num_day_lactation_0_100
from functions_Bjorn import num_day_lactation_101_200
from functions_Bjorn import num_day_lactation_201_up
from functions_Bjorn import avg_milking_volume_lact_0_100
from functions_Bjorn import avg_milking_volume_lact_101_200
from functions_Bjorn import avg_milking_volume_lact_201_up

files="extractions/extraction_DelPro-5.3_20201102_03-10/GIGACOW_milkings_v2_20201102.csv","extractions/extraction_DelPro-5.3_20201103_03-10/GIGACOW_milkings_v2_20201103.csv", "extractions/extraction_DelPro-5.3_20201104_03-10/GIGACOW_milkings_v2_20201104.csv"

data = pd.concat((pd.read_csv(filename, sep = ';', decimal=',', header = 1) for filename in files), ignore_index = True)

data2 = pd.read_csv("extractions/extraction_DelPro-5.3_20201104_03-10/GIGACOW_feed_v1_20201104 001000.csv", encoding='latin-1')
data3 = pd.read_csv("extractions/extraction_DelPro-5.3_20201104_03-10/GIGACOW_identity_v1_20201104 002001.csv")

print('Average 7 days, nr of kickOffs: ', avg_kickOffs(data['Starttid'], data['Avspark']))
print('Average 7 days, time in robot: ', avg_in_robot(data['Mjölkningstid (mm:ss)']))
print('Milk to tank yesterday: ', milk_to_tank_today(data['Starttid'], data['Mjölkdestination'], data['Mjölkmängd (kg)']))

print('Average 7 days, milking Volym. ', num_day_lactation_0_100(data2['Days In Milk']), ' cows in lactation 0-100: ', avg_milking_volume_lact_0_100(data['Starttid'], data['Djurnr'], data['Åtgärd'], data['Mjölkmängd (kg)'], data3['Animal Number'], data3['Official Reg. No. (ORN)'], data2['Official Reg. No. (ORN)'], data2['Days In Milk']))
print('Average 7 days, milking Volym. ', num_day_lactation_101_200(data2['Days In Milk']), ' cows in lactation 101-200: ', avg_milking_volume_lact_101_200(data['Starttid'], data['Djurnr'], data['Åtgärd'], data['Mjölkmängd (kg)'], data3['Animal Number'], data3['Official Reg. No. (ORN)'], data2['Official Reg. No. (ORN)'], data2['Days In Milk']))
print('Average 7 days, milking Volym. ', num_day_lactation_201_up(data2['Days In Milk']), ' cows in lactation 200-: ', avg_milking_volume_lact_201_up(data['Starttid'], data['Djurnr'], data['Åtgärd'], data['Mjölkmängd (kg)'], data3['Animal Number'], data3['Official Reg. No. (ORN)'], data2['Official Reg. No. (ORN)'], data2['Days In Milk']))

