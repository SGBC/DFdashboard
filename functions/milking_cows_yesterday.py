import pandas as pd


# Input: pandas DataFrame for date and total_milk_yield (per cow)
# Output: Number of milking cows producing more than 0 kg of milk at least once based on the most recent day (yesterday)
def nr_of_milking_cows_yesterday(date, total_milk_yield):

    # Concatenate data
    data = pd.concat([date, total_milk_yield], axis = 1)

    # Drop rows which are milking an amount equal to 0 kg
    data = data.drop(data[data['Total_milk_yield'] == 0.00].index)

    # Get the data for the most recent day (yesterday)
    data_yesterday = data[data['Date'] == data['Date'].iloc[-1]]
    
    return len(data_yesterday)

# Input: pandas DataFrame for date, milk_yield and Milk_destination
# Output: milk to tank yesterday
def milk_to_tank_yesterday(date, Milk_yield, Milk_destination):
    
    # Concatenate data
    data = pd.concat([date, Milk_yield, Milk_destination], axis = 1)

    # Removes data from other days and not going to tank
    data = data[data["Date"] == data["Date"].iloc[-1]]
    data = data[data["Milk_destination"] == 1]

    return round(data['Milk_yield'].sum(),2)