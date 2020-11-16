import pandas as pd
from functions_Axel import avg_milking_volume_per_cow as avg_volume
from functions_Axel import avg_nr_of_milkings_per_cow as avg_milkings
from functions_Axel import nr_of_milking_cows_yesterday as nr_cows
from functions_Axel import cumulative_milk_volume as total_milk
from functions_Axel import avg_milk_from_robots as robot_milk

# Read data
files = [r'extractions/extraction_DelPro-5.3_20201102_03-10/GIGACOW_milkings_v2_20201102.csv',
        r'extractions/extraction_DelPro-5.3_20201103_03-10/GIGACOW_milkings_v2_20201103.csv',
        r'extractions/extraction_DelPro-5.3_20201104_03-10/GIGACOW_milkings_v2_20201104.csv']
data = pd.concat((pd.read_csv(filename, sep = ';', header = 1) for filename in files), ignore_index = True)
print(data)

# Get average milking volume per cow per day
milk_weight = data['Mjölkmängd (kg)'].str.replace(',', '.').astype(float)
avg_milking_volume_per_cow = avg_volume(data['Starttid'], data['Djurnr'], data['Åtgärd'], milk_weight)
print('Average milking volume per cow per day: ', avg_milking_volume_per_cow)

# Get average number of milkings per cow per day
avg_nr_of_milkings_per_cow = avg_milkings(data['Starttid'], data['Djurnr'], data['Åtgärd'])
print('Average number of milkings per cow per day: ', avg_nr_of_milkings_per_cow)

# Get number of milking cows yesterday
nr_of_milking_cows_yesterday = nr_cows(data['Starttid'], data['Djurnr'], data['Åtgärd'], milk_weight)
print('Number of milking cows yesterday: ', nr_of_milking_cows_yesterday)

# Get cumulative milk volume
cumulative_milk_volume = total_milk(milk_weight)
print('Cumulative milk volume: ', cumulative_milk_volume)

# Get average milking volume per robot and show average daily milk volume
milk_from_robot = robot_milk(data['Starttid'], data['MS/MP'], data['Åtgärd'], milk_weight)
print('Average milk from ', milk_from_robot[0], ": ", milk_from_robot[1])
print('Average milk from ', milk_from_robot[2], ": ", milk_from_robot[3])
print('Average milk from ', milk_from_robot[0], " and ", milk_from_robot[2], ": ", milk_from_robot[1] + milk_from_robot[3])