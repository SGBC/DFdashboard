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