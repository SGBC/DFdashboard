import pandas as pd


# Input: pandas DataFrame containing all raw milking data
# Output: pandas DataFrame containing formatted milking data
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
    
    # Map kickOffs to ones, otherwise zero
    data['Nr_of_kickOffs'] = (data['Nr_of_kickOffs'].isnull()).replace({True: 0, False: 1})

    return data


# Input: pandas DataFrame containing all raw traffic data
# Output: pandas DataFrame containing formatted traffic data
def preprocess_traffic(data):

    # Rename columns
    data = data.rename(columns = {'Animal Number':'Animal_ID', 'Group Name':'Group', 'Date/Time':'Date'})

    # Drop rows containing null values as dates and convert date format
    data = data[data['Date'].notna()]
    data['Date'] = pd.to_datetime(data['Date']).dt.strftime('%Y-%m-%d')

    # Result containing Pass or Separated count as passing the smartgate
    data['Result'].loc[data['Result'].str[0:4] == "Pass"] = 1
    data['Result'].loc[data['Result'].str[0:9] == "Separated"] = 1
    data['Result'] = (data['Result'] == 1).replace({True: 1, False: 0})

    return data


# Input: pandas DataFrame containing all raw feed data
# Output: pandas DataFrame containing formatted feed data
def preprocess_feed(data):

    # Rename columns
    data = data.rename(columns = {'Official Reg. No. (ORN)':'Official Animal ID'})

    # Get grain column names
    col_names = list(data)
    grain_col_names = []
    for col in col_names:
        if (col[0:4] == "Giva"):
            grain_col_names.append(col)

    # Get the grain columns and sum them for each cow
    total_grain_dispensed = data[grain_col_names].transpose().sum()
    data['Total Grain Dispensed'] = total_grain_dispensed

    return data.loc[:, ['Official Animal ID', 'Lactation Number', 'Days In Milk', 'Last Calving Date', 'Concentrates Ration Yesterday', 'Total Grain Dispensed']]
