import pandas as pd
import re


# Input: pandas DataFrame for 
# Output: pandas DataFrame for 
def cow_stat(animal_id, start_time, milkTime, action, milk, kickOff, animal_id2, off_id, off_id2, lact):
    
    # Concatenate data
    data = pd.concat([start_time, animal_id, milkTime, action, milk, kickOff], axis = 1)
    data2 = pd.concat([animal_id2, off_id], axis = 1)
    data3 = pd.concat([off_id2, lact], axis = 1)

    data2 =  pd.merge(data2, data3)

    # Get the unique cows
    cow_id = pd.unique(data['Animal_ID'])

    outData = pd.DataFrame(cow_id, columns=['Animal_ID'])

    for i in outData['Animal_ID']:
        outData.loc[outData.Animal_ID == i, "numberOfMilkings"] = ((data[data['Animal_ID']==i])['Action']).sum()
        time=(data[data['Animal_ID']==i])['Milk_duration']
        times=[]
        for j in time:
            temp = re.findall(r'\d+', j)
            times.append(float(temp[0])+float(temp[1])/60)
        outData.loc[outData.Animal_ID == i, "avg_time"] = round(sum(times)/len(times),2)
        outData.loc[outData.Animal_ID == i, "total_Milk"] = (data[data['Animal_ID']==i])['Milk_yield'].sum()
        outData.loc[outData.Animal_ID == i, "numberOfkickOffs"] = (outData[outData['Animal_ID']==i])["numberOfMilkings"] -(data[data['Animal_ID']==i])['Nr_of_kickOffs'].isnull().sum()

    data2 = data2.rename(columns={'Animal Number': 'Animal_ID'})
    outData = pd.merge(outData, data2)
    outData = outData.drop(columns=['Official Reg. No. (ORN)'])

    return outData