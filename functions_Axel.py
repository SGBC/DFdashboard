import pandas as pd

milk_density = 1.034


# Input: pandas DataFrame for start_time, animal_id, action and milk_weight
# Output: Average milking volume per cow per day based on the number of dates present in the data
def avg_milking_volume_per_cow(start_time, animal_id, action, milk_weight):

    # Concatenate data
    data = pd.concat([start_time, animal_id, action, milk_weight], axis = 1)

    # Drop rows which are not milking
    data = data.drop(data[data['Åtgärd'] != 'Mjölkning'].index)
    data = data.reset_index(drop = True)

    # Get the unique dates
    dates = pd.unique(data['Starttid'].str[0:10])

    # Calculate the total number of milked cows by summing the daily number of milked cows
    total_nr_of_milked_cows = 0
    for date in dates:
        daily_data = data[data['Starttid'].str[0:10] == date]
        daily_nr_of_milked_cows = pd.unique(daily_data['Djurnr'])
        total_nr_of_milked_cows += len(daily_nr_of_milked_cows)
    
    # Calculate average
    avg = data['Mjölkmängd (kg)'].sum()/total_nr_of_milked_cows

    return avg/milk_density


# Input: pandas DataFrame for start_time, animal_id and action
# Output: Average number of milkings per cow per day based on the number of dates present in the data
def avg_nr_of_milkings_per_cow(start_time, animal_id, action):

    # Concatenate data
    data = pd.concat([start_time, animal_id, action], axis = 1)

    # Drop rows which are not milking
    data = data.drop(data[data['Åtgärd'] != 'Mjölkning'].index)
    data = data.reset_index(drop = True)

    # Get the unique dates
    dates = pd.unique(data['Starttid'].str[0:10])

    # Calculate the total number of milked cows by summing the daily number of milked cows
    total_nr_of_milked_cows = 0
    for date in dates:
        daily_data = data[data['Starttid'].str[0:10] == date]
        daily_nr_of_milked_cows = pd.unique(daily_data['Djurnr'])
        total_nr_of_milked_cows += len(daily_nr_of_milked_cows)
    
    return len(data)/total_nr_of_milked_cows


# Input: pandas DataFrame for start_time, animal_id, action and milk_weight
# Output: Number of milking cows producing more than 0 kg of milk at least once based on the most recent day (yesterday)
def nr_of_milking_cows_yesterday(start_time, animal_id, action, milk_weight):
    
    # Concatenate data
    data = pd.concat([start_time, animal_id, action, milk_weight], axis = 1)

    # Drop rows which are not milking or milking an amount equal to 0 kg
    data = data.drop(data[data['Åtgärd'] != 'Mjölkning'].index)
    data = data.drop(data[data['Mjölkmängd (kg)'] == 0.00].index)
    data = data.reset_index(drop = True)

    # Get the unique dates and data for the most recent date
    dates = pd.unique(data['Starttid'].str[0:10])
    most_recent_date_data = data[data['Starttid'].str[0:10] == dates[-1]]

    return len(pd.unique(most_recent_date_data['Djurnr']))


# Input: pandas DataFrame for milk_weight
# Output: Cumulative milk volume
def cumulative_milk_volume(milk_weight):
    return milk_weight.sum()/milk_density


# Input: pandas DataFrame for start_time, animal_id, action and milk_weight
# Output: List containing robot name followed by the average daily milk volume, for each robot
def avg_milk_from_robots(start_time, robot, action, milk_weight):

    # Concatenate data
    data = pd.concat([start_time, robot, action, milk_weight], axis = 1)

    # Drop rows which are not milking
    data = data.drop(data[data['Åtgärd'] != 'Mjölkning'].index)

    # Get the unique dates and robot names
    dates = pd.unique(data['Starttid'].str[0:10])
    robot_names = pd.unique(data['MS/MP'])

    # Calculate the daily average milk volume received by each robot
    avg_milk_by_robot = []
    for robot in robot_names:
        robot_data = data[data['MS/MP'] == robot]
        avg_milk = robot_data['Mjölkmängd (kg)'].sum()/(len(dates)*milk_density)
        avg_milk_by_robot.append(robot)
        avg_milk_by_robot.append(avg_milk)
    
    return avg_milk_by_robot