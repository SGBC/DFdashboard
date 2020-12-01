import pandas as pd


# Input: pandas DataFrame for date, animal_id, action and milk_yield
# Output: pandas DataFrame containing date, animal_id, daily_milk_yield and nr_of_milkings
def daily_milk_per_cow(date, animal_id, action, milk_yield):

    # Concatenate data
    data = pd.concat([date, animal_id, action, milk_yield], axis = 1)

    # Drop rows which are not milking
    data = data.drop(data[data['Action'] != 1].index)

    # Get the unique dates
    dates = pd.unique(data['Date'])

    # Calculate the total milk produced by each cow for each day
    return_data = pd.DataFrame(columns = ['Date', 'Animal_ID', 'Milk_yield', 'Nr_of_milkings'])
    for date in dates:
        daily_data = data[data['Date'] == date]
        daily_milked_cows = pd.unique(daily_data['Animal_ID'])
        for cow in daily_milked_cows:
            daily_milkings = daily_data[daily_data['Animal_ID'] == cow]
            daily_milk = daily_milkings['Milk_yield'].sum()
            daily_nr_milkings = len(daily_milkings)
            return_data = return_data.append({'Date': date, 'Animal_ID': cow, 'Milk_yield': daily_milk, 'Nr_of_milkings': daily_nr_milkings}, ignore_index = True)
    
    return return_data


# Input: pandas DataFrame for date, animal_id, action and milk_yield
# Output: Average daily milk per cow based on the number of dates present in the data
def avg_daily_milk_per_cow(date, animal_id, action, milk_yield):

    # Get daily milk per cow
    data = daily_milk_per_cow(date, animal_id, action, milk_yield)

    return data['Milk_yield'].sum()/len(data)