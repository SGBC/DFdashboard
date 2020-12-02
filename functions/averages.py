import pandas as pd
import re


# Input: pandas DataFrame for total_milk_yield (per cow)
# Output: Average daily milk yield per cow
def avg_daily_milk_per_cow(total_milk_yield):
    return total_milk_yield.sum()/len(total_milk_yield)


# Input: pandas DataFrame for date, animal_id, action and milk_yield
# Output: List containing robot name followed by the average received daily milk yield, for each robot
def avg_milk_from_robots(date, robot, action, milk_yield):

    # Concatenate data
    data = pd.concat([date, robot, action, milk_yield], axis = 1)

    # Drop rows which are not milking
    data = data.drop(data[data['Action'] != 1].index)

    # Get the unique dates and robot names
    dates = pd.unique(data['Date'])
    robot_names = pd.unique(data['Robot'])

    # Calculate the daily average milk yield received by each robot
    avg_milk_by_robot = []
    for robot in robot_names:
        robot_data = data[data['Robot'] == robot]
        avg_milk = robot_data['Milk_yield'].sum()/len(dates)
        avg_milk_by_robot.append(robot)
        avg_milk_by_robot.append(avg_milk)
    
    return avg_milk_by_robot


# Input: pandas DataFrame for nr_of_milkings (per cow)
# Output: Average daily number of milkings per cow
def avg_nr_of_milkings_per_cow(nr_of_milkings):
    return nr_of_milkings.sum()/len(nr_of_milkings)


# Input: pandas DataFrame for animal_id, date and the result from communicating with the smartgate
# Output: Average number of smartgate passes based on the number of dates present in the data
def avg_nr_pass_smartgate(animal_id, date, result):

    # Concatenate data
    data = pd.concat([animal_id, date, result], axis = 1)

    # Get rows which resulted in pass
    data = data[data['Result'] == 1]

    # Get the unique dates
    dates = pd.unique(data['Date'])

    # For each date, compute how many cows have passed the smartgate
    active_cows = 0
    for date in dates:
        active_cows += len(pd.unique(data[data['Date'] == date]['Animal_ID']))
    
    return len(data)/active_cows


# Input: pandas DataFrame for milking_time
# Output: Average milking time per milking event logged
def avg_time_in_robot(timeInRobot):
    times=[]
    for i in timeInRobot:
        temp = re.findall(r'\d+', i)
        times.append(float(temp[0])+float(temp[1])/60)
    return pd.DataFrame(times).mean()[0]


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
    data = data[data['Animal_ID'].isin(data2['Animal Number'])]
    
    # Get the unique dates and cows
    dates = pd.unique(data['Date'])
    cow_id = pd.unique(data['Animal_ID'])

    # Calculate average
    avg = data['Milk_yield'].sum()/(len(dates)*len(cow_id))

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
    data = data[data['Animal_ID'].isin(data2['Animal Number'])]
    
    # Get the unique dates and cows
    dates = pd.unique(data['Date'])
    cow_id = pd.unique(data['Animal_ID'])

    # Calculate average
    avg = data['Milk_yield'].sum()/(len(dates)*len(cow_id))

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
    data = data[data['Animal_ID'].isin(data2['Animal Number'])]
    
    # Get the unique dates and cows
    dates = pd.unique(data['Date'])
    cow_id = pd.unique(data['Animal_ID'])

    # Calculate average
    avg = data['Milk_yield'].sum()/(len(dates)*len(cow_id))

    return avg
