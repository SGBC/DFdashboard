import numpy as np
import pandas as pd
import re



# Input: pandas DataFrame for start_time
# Output: pandas DataFrame for year, month, day, hour, minute
def dates(date):
    dates=[]
    for i in date:
        temp = re.findall(r'\d+', i)
        dates.append(temp)

    return pd.DataFrame(dates,columns=['y', 'm', 'd', 'tim', 'min'])

# Input: pandas DataFrame for year, month, day, hour, minute
# Output: number of days
def num_days(date):
    date=date.drop(columns=['tim', 'min'])
    date = date.drop_duplicates()
    num = date.count()[0]
    return num

#Avspark kickoff?
#Per cow?
# Input: pandas DataFrame for kickOff
# Output: number of KickOffs
def num_kickOffs(kickOff):
    kick= kickOff.isnull().sum()
    return kickOff.size-kick

# Input: pandas DataFrame for start_time, kickOff
# Output: Average kickOffs based on the number of dates present in the data
def avg_kickOffs(start_time, kickOff):
    return num_kickOffs(kickOff)/num_days(dates(start_time))

# Input: pandas DataFrame for milking_time
# Output: pandas DataFrame with milking times in minutes
def time_to_min(time):
    times=[]
    for i in time:
        temp = re.findall(r'\d+', i)
        times.append(float(temp[0])+float(temp[1])/60)
    return pd.DataFrame(times)

#omjölkad time counted?
#Per cow? Per time?
# Input: pandas DataFrame for milking_time
# Output: Average milking time per milking event logged
def avg_in_robot(timeInRobot):
    return time_to_min(timeInRobot).mean()[0]

# Input: pandas DataFrame for for year, month, day, hour, minute
# Output: Latest date found as string in format yyyy-mm-dd
def today(dates):
    date=dates.drop(columns=['tim', 'min'])
    date = date.drop_duplicates()
    date = date[date['y'] == date['y'].max()]
    date = date[date['m'] == date['m'].max()]
    date = date[date['d'] == date['d'].max()]
    return '' + date['y'].values[0] + '-' + date['m'].values[0] + '-' + date['d'].values[0]

# Input: pandas DataFrame for start_time, milk destination and milk_weight
# Output: Milk volume to tank for the latest date found
def milk_to_tank_today(start_time, milkdest, milk):
    
    # Concatenate data
    data = pd.concat([start_time, milkdest, milk], axis = 1)

    # Removes data from other days
    day=today(dates(data['Starttid']))
    data = data[data["Starttid"].str.contains(day, na=False)]

    # Calculate total milk to tank
    milk = data.loc[data['Mjölkdestination']=='Mjölktank', 'Mjölkmängd (kg)'].sum()
    return milk

# Input: pandas DataFrame for DaysInMilk
# Output: Number off cows who has been in milk up to 100 days
def num_day_lactation_0_100(DaysInMilk):
    return (DaysInMilk<=100).sum()

# Input: pandas DataFrame for DaysInMilk
# Output: Number off cows who has been in milk between 101 and 200 days.
def num_day_lactation_101_200(DaysInMilk):
    return (DaysInMilk[DaysInMilk<=200]>100).sum()

# Input: pandas DataFrame for DaysInMilk
# Output: Number off cows who has been in milk more than 200 days
def num_day_lactation_201_up(DaysInMilk):
    return (DaysInMilk>200).sum()

# Input: pandas DataFrame for start_time, animal_id, action and milk_weight, 
#        pandas DataFrame for animal_id and official ID
#        pandas DataFrame for official ID and number of days in milk
# Output: Average milking volume per cow who has been in milk up to 100 days based on the number of dates present in the data
def avg_milking_volume_lact_0_100(start_time, animal_id, action, milk, animal_id2, off_id, off_id2, lact):

    # Concatenate data
    data = pd.concat([start_time, animal_id, action, milk], axis = 1)
    data2 = pd.concat([animal_id2, off_id], axis = 1)
    data3 = pd.concat([off_id2, lact], axis = 1)

    # Removes all cows who doesn't fit the criteria
    data3 = data3[data3['Days In Milk'] <= 100]  
    data2 = data2[data2['Official Reg. No. (ORN)'].isin(data3['Official Reg. No. (ORN)'])]
    data = data[data['Djurnr'].isin(data2['Animal Number'])]
    
    # Get the unique dates and cows
    dates = pd.unique(data['Starttid'].str[0:10])
    cow_id = pd.unique(data['Djurnr'])

    # Calculate average
    avg = data['Mjölkmängd (kg)'].sum()/(len(dates)*len(cow_id))

    return avg

# Input: pandas DataFrame for start_time, animal_id, action and milk_weight, 
#        pandas DataFrame for animal_id and official ID
#        pandas DataFrame for official ID and number of days in milk
# Output: Average milking volume per cow who has been in milk between 101 and 200 days based on the number of dates present in the data
def avg_milking_volume_lact_101_200(start_time, animal_id, action, milk, animal_id2, off_id, off_id2, lact):

    # Concatenate data
    data = pd.concat([start_time, animal_id, action, milk], axis = 1)
    data2 = pd.concat([animal_id2, off_id], axis = 1)
    data3 = pd.concat([off_id2, lact], axis = 1)

    # Removes all cows who doesn't fit the criteria
    data3 = data3[data3['Days In Milk'] > 100]  
    data3 = data3[data3['Days In Milk'] <= 200]
    data2 = data2[data2['Official Reg. No. (ORN)'].isin(data3['Official Reg. No. (ORN)'])]
    data = data[data['Djurnr'].isin(data2['Animal Number'])]
    
    # Get the unique dates and cows
    dates = pd.unique(data['Starttid'].str[0:10])
    cow_id = pd.unique(data['Djurnr'])

    # Calculate average
    avg = data['Mjölkmängd (kg)'].sum()/(len(dates)*len(cow_id))

    return avg

# Input: pandas DataFrame for start_time, animal_id, action and milk_weight, 
#        pandas DataFrame for animal_id and official ID
#        pandas DataFrame for official ID and number of days in milk
# Output: Average milking volume per cow who has been in milk more than 200 days based on the number of dates present in the data
def avg_milking_volume_lact_201_up(start_time, animal_id, action, milk, animal_id2, off_id, off_id2, lact):

    # Concatenate data
    data = pd.concat([start_time, animal_id, action, milk], axis = 1)
    data2 = pd.concat([animal_id2, off_id], axis = 1)
    data3 = pd.concat([off_id2, lact], axis = 1)

    # Removes all cows who doesn't fit the criteria
    data3 = data3[data3['Days In Milk'] > 200]  
    data2 = data2[data2['Official Reg. No. (ORN)'].isin(data3['Official Reg. No. (ORN)'])]
    data = data[data['Djurnr'].isin(data2['Animal Number'])]
    
    # Get the unique dates and cows
    dates = pd.unique(data['Starttid'].str[0:10])
    cow_id = pd.unique(data['Djurnr'])

    # Calculate average
    avg = data['Mjölkmängd (kg)'].sum()/(len(dates)*len(cow_id))

    return avg

