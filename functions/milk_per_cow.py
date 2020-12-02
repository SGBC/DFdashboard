import pandas as pd
import re


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
    return_data = pd.DataFrame(columns = ['Date', 'Animal_ID', 'Total_milk_yield', 'Nr_of_milkings'])
    for date in dates:
        daily_data = data[data['Date'] == date]
        daily_milked_cows = pd.unique(daily_data['Animal_ID'])
        for cow in daily_milked_cows:
            daily_milkings = daily_data[daily_data['Animal_ID'] == cow]
            daily_milk = daily_milkings['Milk_yield'].sum()
            daily_nr_milkings = len(daily_milkings)
            return_data = return_data.append({'Date': date, 'Animal_ID': cow, 'Total_milk_yield': daily_milk, 'Nr_of_milkings': daily_nr_milkings}, ignore_index = True)
    
    return return_data


# Input: pandas DataFrame for date, animal_id, Milk_duration, action, milk_yield and Nr_of_kickOffs
#        pandas DataFrame for animal_id and official ID
#        pandas DataFrame for official ID and number of days in milk
# Output: pandas DataFrame containing date, animal_id, daily_milk_yield, nr_of_milkings, nr_of_kickoffs and days_in_milk
def cow_stat(date, animal_id, Milk_duration, action, milk_yield, Nr_of_kickOffs, animal_id2, off_id, off_id2, lact):
    
    data = daily_milk_per_cow(date, animal_id, action, milk_yield)

    # Concatenate data
    data1 = pd.concat([date, animal_id, Milk_duration, action, Nr_of_kickOffs], axis = 1)
    data2 = pd.concat([animal_id2, off_id], axis = 1)
    data3 = pd.concat([off_id2, lact], axis = 1)

    data2 =  pd.merge(data2, data3)

    # Drop rows which are not milking
    data1 = data1.drop(data1[data1['Action'] != 1].index)

    # Get the unique dates
    dates = pd.unique(data['Date'])

    # Calculate the number of kickoffs and average milking duration by each cow for each day
    return_data = pd.DataFrame(columns = ['Date', 'Animal_ID', 'avg_Milk_duration', 'Nr_of_kickOffs'])
    for date in dates:
        daily_data = data1[data1['Date'] == date]
        daily_milked_cows = pd.unique(daily_data['Animal_ID'])
        for cow in daily_milked_cows:
            daily_milkings = daily_data[daily_data['Animal_ID'] == cow]
            times=[]
            for time in daily_milkings['Milk_duration']:
                temp = re.findall(r'\d+', time)
                times.append(float(temp[0])+float(temp[1])/60)
            avg_Milk_duration = round(sum(times)/len(times),2)
            Nr_of_kickOffs = daily_milkings['Nr_of_kickOffs'].sum()
            return_data = return_data.append({'Date': date, 'Animal_ID': cow, 'avg_Milk_duration': avg_Milk_duration, 'Nr_of_kickOffs': Nr_of_kickOffs}, ignore_index = True)

    # Merges data to one dataframe
    data2 = data2.rename(columns={'Animal Number': 'Animal_ID'})
    return_data = pd.merge(return_data, data2)
    return_data = return_data.drop(columns=['Official Reg. No. (ORN)'])
    data = pd.merge(data, return_data)

    return data
