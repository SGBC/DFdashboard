import pandas as pd

# Input: pandas DataFrame for kickOff
# Output: number of KickOffs
def num_kickOffs(kickOff):
    kick= kickOff.isnull().sum()
    return kickOff.size-kick

# Input: pandas DataFrame for start_time, kickOff
# Output: Average kickOffs based on the number of dates present in the data
def avg_kickOffs(start_time, kickOff):
    return num_kickOffs(kickOff)/len(pd.unique(start_time))