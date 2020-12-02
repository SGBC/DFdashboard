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
