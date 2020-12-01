import pandas as pd
import re

# Input: pandas DataFrame for milking_time
# Output: Average milking time per milking event logged
def avg_in_robot(timeInRobot):
    times=[]
    for i in timeInRobot:
        temp = re.findall(r'\d+', i)
        times.append(float(temp[0])+float(temp[1])/60)
    pd.DataFrame(times)
    return pd.DataFrame(times).mean()[0]