import pandas as pd
import glob
import functions as func

days=7
out_data = pd.DataFrame(columns = ['Date','avg_daily_milk_per_cow', 'avg_daily_nr_of_milkings_per_cow',
    'nr_of_milkings_cows_yesterday', 'avg_milk_from_vms_1', 'avg_milk_from_vms_2', 'avg_milk_from_vms_1_and_2',
    'avg_nr_pass_smartgate', 'projected_monthly_milk', 'avg_nr_of_kickOffs','avg_time_in_robot',
    'Milk_to_tank_yesterday','cows_lactation_day_0-100','cows_lactation_day_101-200','cows_lactation_day_201-',
    'avg_milking_volume_lact_0-100','avg_milking_volume_lact_101-200', 'avg_milking_volume_lact_201-'])

# Add offset in order to compute different values for different dates
for offset in range(9):
    
    files = []
    files2 = []
    
    # Read milking and cow traffic data for seven days
    for i in range(days):
        if (i+offset)<8:
            files.append(glob.glob("extractions/extraction_DelPro-5.3_2020110{}_03-10/GIGACOW_milkings*.csv".format(i+2+offset))[0])
            files2.append(glob.glob("extractions/extraction_DelPro-5.3_2020110{}_03-10/Cow Traffic*.csv".format(i+2+offset))[0])
        else:
            files.append(glob.glob("extractions/extraction_DelPro-5.3_202011{}_03-10/GIGACOW_milkings*.csv".format(i+2+offset))[0])
            files2.append(glob.glob("extractions/extraction_DelPro-5.3_202011{}_03-10/Cow Traffic*.csv".format(i+2+offset))[0])
    
    data_milkings = pd.concat((pd.read_csv(filename, sep = ';', decimal=',', header = 1) for filename in files), ignore_index = True)
    data_traffic = pd.concat((pd.read_csv(filename, sep = ',', encoding='latin-1') for filename in files2), ignore_index = True)

    # Read feed and identity data
    if (offset)<2:
        data_feed = pd.read_csv(glob.glob("extractions/extraction_DelPro-5.3_2020110{}_03-10/GIGACOW_feed*.csv".format(days+1+offset))[0], encoding='latin-1')
        data_identity = pd.read_csv(glob.glob("extractions/extraction_DelPro-5.3_2020110{}_03-10/GIGACOW_identity*.csv".format(days+1+offset))[0])
    else:
        data_feed = pd.read_csv(glob.glob("extractions/extraction_DelPro-5.3_202011{}_03-10/GIGACOW_feed*.csv".format(days+1+offset))[0], encoding='latin-1')
        data_identity = pd.read_csv(glob.glob("extractions/extraction_DelPro-5.3_202011{}_03-10/GIGACOW_identity*.csv".format(days+1+offset))[0])

    
    # Preprocess milking and cow traffic data
    data_milkings = func.preprocess_milkings(data_milkings)
    data_traffic = func.preprocess_traffic(data_traffic)

    # Lump together daily milkings by the same cow into one total daily milk yield per cow
    data_cow = func.daily_milk_per_cow(data_milkings['Date'], data_milkings['Animal_ID'], data_milkings['Action'], data_milkings['Milk_yield'])
    
    # Compute key values
    v = data_milkings['Date'].iloc[-1] #Most recent date
    w1 = func.avg_daily_milk_per_cow(data_cow['Total_milk_yield']) #"avg_daily_milk_per_cow"
    w2 = func.avg_nr_of_milkings_per_cow(data_cow['Nr_of_milkings']) #"avg_daily_nr_of_milkings_per_cow"
    w3 = func.nr_of_milking_cows_yesterday(data_cow['Date'], data_cow['Total_milk_yield']) #"nr_of_milkings_cows_yesterday"

    milk_from_robot = func.avg_milk_from_robots(data_milkings['Date'], data_milkings['Robot'], data_milkings['Action'], data_milkings['Milk_yield'])
    
    w4 = milk_from_robot[1] #"avg_milk_from_vms_1"
    w5 = milk_from_robot[3] #"avg_milk_from_vms_2"
    w6 = milk_from_robot[-1] #"avg_milk_from_vms_1_and_2"

    w7 = func.avg_nr_pass_smartgate(data_traffic['Animal_ID'], data_traffic['Date'], data_traffic['Result']) #"avg_nr_pass_smartgate"
    w8 = func.proj_monthly_milk(milk_from_robot) #projected_monthly_milk

    v1 = func.avg_kickOffs(data_milkings['Date'], data_milkings['Animal_ID'], data_milkings['Nr_of_kickOffs'])
    v2 = func.avg_time_in_robot(data_milkings['Milk_duration'])
    v3 = func.milk_to_tank_yesterday(data_milkings['Date'], data_milkings['Milk_yield'], data_milkings['Milk_destination'])
    v4 = func.num_day_lactation_0_100(data_feed['Days In Milk'])
    v5 = func.num_day_lactation_101_200(data_feed['Days In Milk'])
    v6 = func.num_day_lactation_201_up(data_milkings['Animal_ID'], data_milkings['Milk_yield'], data_identity['Animal Number'], data_identity['Official Reg. No. (ORN)'], data_feed['Official Reg. No. (ORN)'], data_feed['Days In Milk'])
    v7 = func.avg_milking_volume_lact_0_100(data_milkings['Date'], data_milkings['Animal_ID'], data_milkings['Action'], data_milkings['Milk_yield'], data_identity['Animal Number'], data_identity['Official Reg. No. (ORN)'], data_feed['Official Reg. No. (ORN)'], data_feed['Days In Milk'])
    v8 = func.avg_milking_volume_lact_101_200(data_milkings['Date'], data_milkings['Animal_ID'], data_milkings['Action'], data_milkings['Milk_yield'], data_identity['Animal Number'], data_identity['Official Reg. No. (ORN)'], data_feed['Official Reg. No. (ORN)'], data_feed['Days In Milk'])
    v9 = func.avg_milking_volume_lact_201_up(data_milkings['Date'], data_milkings['Animal_ID'], data_milkings['Action'], data_milkings['Milk_yield'], data_identity['Animal Number'], data_identity['Official Reg. No. (ORN)'], data_feed['Official Reg. No. (ORN)'], data_feed['Days In Milk'])


    # Append all key values to a DataFrame
    out_data = out_data.append({'Date': v, 'avg_daily_milk_per_cow': w1, 'avg_daily_nr_of_milkings_per_cow': w2, 
        'nr_of_milkings_cows_yesterday': w3, 'avg_milk_from_vms_1': w4, 'avg_milk_from_vms_2': w5,
        'avg_milk_from_vms_1_and_2': w6, 'avg_nr_pass_smartgate': w7, 'projected_monthly_milk': w8,
        'avg_nr_of_kickOffs': v1,'avg_time_in_robot': v2,'Milk_to_tank_yesterday': v3,'cows_lactation_day_0-100': v4,
        'cows_lactation_day_101-200': v5,'cows_lactation_day_201-': v6,'avg_milking_volume_lact_0-100': v7,
        'avg_milking_volume_lact_101-200': v8, 'avg_milking_volume_lact_201-': v9}, ignore_index = True)

# Write key values to a csv file
out_data.to_csv("keyvalues.csv", index=False)
out_data.to_csv("keyvaluesOverView.csv", index=False, sep = ';')

stat = func.cow_stat_kickoffs(data_milkings['Date'], data_milkings['Animal_ID'], data_milkings['Milk_duration'], data_milkings['Action'], data_milkings['Milk_yield'], data_milkings['Nr_of_kickOffs'], data_identity['Animal Number'], data_identity['Official Reg. No. (ORN)'], data_feed['Official Reg. No. (ORN)'], data_feed['Days In Milk'])
(stat[stat['Nr_of_kickOffs']>2]).to_csv("kickOffs.csv", index=False)

stat_milking_once_below_thresh = func.milking_once_below_thresh(data_cow['Date'], data_cow['Animal_ID'], data_cow['Total_milk_yield'], data_cow['Nr_of_milkings'], 20)
stat_milking_more_below_thresh = func.milking_more_below_thresh(data_cow['Date'], data_cow['Animal_ID'], data_cow['Total_milk_yield'], data_cow['Nr_of_milkings'], 25)

stat_milking_once_below_thresh.to_csv("stat_milking_once_below_thresh.csv", index=False)
stat_milking_more_below_thresh.to_csv("stat_milking_more_below_thresh.csv", index=False)
