import pandas as pd


# Input: pandas DataFrame using per cow data for date, animal_id, milk_yield and nr_of_milkings
#           as well as an integer specifying the milk threshold
# Output: pandas DataFrame specifying cows that have been milked precisely once and below the threshold
def milking_once_below_thresh(date, animal_id, total_milk_yield, nr_of_milkings, threshold):

    # Concatenate data and get the data from the latest date
    data = pd.concat([date, animal_id, total_milk_yield, nr_of_milkings], axis = 1)
    latest = data[data['Date'] == data['Date'].iloc[-1]]

    # Remove cows with more than one milking
    latest = latest[latest['Nr_of_milkings'] == 1]

    return latest.loc[latest['Total_milk_yield'] < threshold].sort_values(by = ['Total_milk_yield']).reset_index(drop = True)


# Input: pandas DataFrame using per cow data for date, animal_id, milk_yield and nr_of_milkings
#           as well as an integer specifying the milk threshold
# Output: pandas DataFrame specifying cows that have been milked twice or more and below the threshold
def milking_more_below_thresh(date, animal_id, total_milk_yield, nr_of_milkings, threshold):

    # Concatenate data and get the data from the latest date
    data = pd.concat([date, animal_id, total_milk_yield, nr_of_milkings], axis = 1)
    latest = data[data['Date'] == data['Date'].iloc[-1]]

    # Remove cows with only one milking
    latest = latest[latest['Nr_of_milkings'] > 1]

    return latest.loc[latest['Total_milk_yield'] < threshold].sort_values(by = ['Total_milk_yield']).reset_index(drop = True)