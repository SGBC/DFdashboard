import pandas as pd


# Input: pandas DataFrame for start_time, kickOff
# Output: Average kickOffs based on the number of dates present in the data
def avg_kickOffs(start_time, Animal_ID, kickOff):
    return round(kickOff.sum()/(len(pd.unique(start_time)) + len(pd.unique(start_time))),2)