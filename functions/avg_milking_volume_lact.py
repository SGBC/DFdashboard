import pandas as pd

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