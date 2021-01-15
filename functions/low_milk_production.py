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

# Input: pandas DataFrame from cow_stats
#           as well as an integer specifying the threshold
# Output: pandas DataFrame specifying cows with more kickoffs than the threshold
def many_kickOffs(stat,threshold):
    return stat[stat['Nr_of_kickOffs']>threshold]

# Input: pandas DataFrame from cow_stats
#           as well as an integer specifying the threshold
# Output: pandas DataFrame specifying cows with longer milk duration than the threshold
def long_milk_duration(stat,threshold):
    return stat[stat['avg_Milk_duration']>threshold]

# Input: pandas DataFrame from cow_stats
#           as well as an integer specifying the threshold
# Output: pandas DataFrame specifying cows with more days in milk than the threshold
def cow_dry_up(stat,threshold):
    
    # Remove cows with less than threshold] days in milk
    stat = stat[stat['Days In Milk']>threshold]

    # Find all unique cows
    cow_id = pd.unique(stat['Animal_ID'])

    # Initialize a DataFrame containing output data
    out_data = pd.DataFrame(columns = ['Animal_ID','avg_milk_yield', 'avg_Nr_of_milkings' , 'avg_Milk_duration', 'Days In Milk'])
    
    # Computes all values for the output
    for cow in cow_id:
        cow_stat = stat[stat['Animal_ID'] == cow]
        out_data = out_data.append({'Animal_ID': cow,'avg_milk_yield': round(sum(cow_stat['Total_milk_yield'])/len(cow_stat['Total_milk_yield']),2),
            'avg_Nr_of_milkings': round(sum(cow_stat['Nr_of_milkings'])/len(cow_stat['Nr_of_milkings']),2),
            'avg_Milk_duration': round(sum(cow_stat['avg_Milk_duration'])/len(cow_stat['avg_Milk_duration']),2),
            'Days In Milk': cow_stat['Days In Milk'].iloc[-1]}, ignore_index = True)

    return out_data