import pandas as pd


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