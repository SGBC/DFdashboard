import pandas as pd


# Input: The output given by avg_milk_from_robots()
# Output: Projected total milk yield for the month given by the latest date
def proj_monthly_milk(avg_milk_robots):

    # Get the daily average milk yield
    avg_milk = avg_milk_robots[-1]

    # Get the number of days in the latest date
    days = pd.Period(avg_milk_robots[-2]).daysinmonth

    return round(avg_milk*days, 2)