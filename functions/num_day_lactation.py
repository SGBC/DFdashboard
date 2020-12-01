import pandas as pd

# Input: pandas DataFrame for DaysInMilk
# Output: Number off cows who has been in milk up to 100 days
def num_day_lactation_0_100(DaysInMilk):
    return (DaysInMilk<=100).sum()

# Input: pandas DataFrame for DaysInMilk
# Output: Number off cows who has been in milk between 101 and 200 days.
def num_day_lactation_101_200(DaysInMilk):
    return (DaysInMilk[DaysInMilk<=200]>100).sum()

# Input: pandas DataFrame for DaysInMilk
# Output: Number off cows who has been in milk more than 200 days
def num_day_lactation_201_up(DaysInMilk):
    return (DaysInMilk>200).sum()
