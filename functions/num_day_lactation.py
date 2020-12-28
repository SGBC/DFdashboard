import pandas as pd

# Input: pandas DataFrame for DaysInMilk
# Output: Number off cows who has been in milk up to 100 days
def num_day_lactation_0_100(DaysInMilk):
    return (DaysInMilk<=100).sum()

# Input: pandas DataFrame for DaysInMilk
# Output: Number off cows who has been in milk between 101 and 200 days.
def num_day_lactation_101_200(DaysInMilk):
    return (DaysInMilk[DaysInMilk<=200]>100).sum()

# Input: pandas DataFrame for animal_id, milk, animal_id2, off_id, off_id2, DaysInMilk
# Output: Number off cows who has been in milk more than 200 days
def num_day_lactation_201_up(animal_id, milk, animal_id2, off_id, off_id2, DaysInMilk):
        
    # Concatenate data
    data = pd.concat([animal_id, milk], axis = 1)
    data2 = pd.concat([animal_id2, off_id], axis = 1)
    data3 = pd.concat([off_id2, DaysInMilk], axis = 1)

    # Removes all cows who doesn't fit the criteria
    data3 = data3[data3['Days In Milk'] > 200]  
    data2 = data2[data2['Official Reg. No. (ORN)'].isin(data3['Official Reg. No. (ORN)'])]
    data = data[data['Animal_ID'].isin(data2['Animal Number'])]

    # Get the unique dates and cows
    cow_id = pd.unique(data['Animal_ID'])
    
    return (cow_id >= 0).sum()
