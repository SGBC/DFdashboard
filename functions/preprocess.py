import pandas as pd


# Input: pandas DataFrame containing all raw milking data
# Output:
def preprocess_milkings(data):

    # Rename columns to English
    data = data.rename(columns = {'Starttid':'Date', 'Djurnr':'Animal_ID', 'Grupp':'Group', 'MS/MP':'Robot', 'Åtgärd':'Action',
                                'Mjölkningstid (mm:ss)':'Milk_duration', 'Mjölkmängd (kg)':'Milk_yield', 'Mjölkningsnummer':'Nr_of_milkings',
                                'Avspark':'Nr_of_kickOffs', 'Mjölkdestination':'Milk_destination'})
    
    # Convert start time to date only
    data['Date'] = data['Date'].str[0:10]

    # Map successful milkings to ones, otherwise zero
    data['Action'] = (data['Action'] == "Mjölkning").replace({True: 1, False: 0})
    
    # Map milkings going to tank to ones, otherwise zero
    data['Milk_destination'] = (data['Milk_destination'] == "Mjölktank").replace({True: 1, False: 0})

    return data
