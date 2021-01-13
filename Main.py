import pandas as pd
import glob
import functions as func

# Initialising dataframe contaning all keyvalues
out_data = pd.DataFrame(columns = ['Date','avg_daily_milk_per_cow', 'avg_daily_nr_of_milkings_per_cow',
    'nr_of_milkings_cows_yesterday', 'avg_milk_from_vms_1', 'avg_milk_from_vms_2', 'avg_milk_from_vms_1_and_2',
    'avg_nr_pass_smartgate', 'projected_monthly_milk', 'avg_nr_of_kickOffs','avg_time_in_robot',
    'Milk_to_tank_yesterday','cows_lactation_day_0-100','cows_lactation_day_101-200','cows_lactation_day_201-',
    'avg_milking_volume_lact_0-100','avg_milking_volume_lact_101-200', 'avg_milking_volume_lact_201-'])

# Add offset in order to compute different values for different dates
for offset in range(9):
    
    files = []
    files2 = []
    
    days=7
    # Read milking and cow traffic data for some days
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
    v0 = data_milkings['Date'].iloc[-1] #Most recent date
    v1 = func.avg_daily_milk_per_cow(data_cow['Total_milk_yield']) #"avg_daily_milk_per_cow"
    v2 = func.avg_nr_of_milkings_per_cow(data_cow['Nr_of_milkings']) #"avg_daily_nr_of_milkings_per_cow"
    v3 = func.nr_of_milking_cows_yesterday(data_cow['Date'], data_cow['Total_milk_yield']) #"nr_of_milkings_cows_yesterday"

    milk_from_robot = func.avg_milk_from_robots(data_milkings['Date'], data_milkings['Robot'], data_milkings['Action'], data_milkings['Milk_yield'])
    
    v4 = milk_from_robot[1] #"avg_milk_from_vms_1"
    v5 = milk_from_robot[3] #"avg_milk_from_vms_2"
    v6 = milk_from_robot[-1] #"avg_milk_from_vms_1_and_2"

    v7 = func.avg_nr_pass_smartgate(data_traffic['Animal_ID'], data_traffic['Date'], data_traffic['Result']) #"avg_nr_pass_smartgate"
    v8 = func.proj_monthly_milk(milk_from_robot) #projected_monthly_milk

    v9 = func.avg_kickOffs(data_milkings['Date'], data_milkings['Animal_ID'], data_milkings['Nr_of_kickOffs'])
    v10 = func.avg_time_in_robot(data_milkings['Milk_duration'])
    v11 = func.milk_to_tank_yesterday(data_milkings['Date'], data_milkings['Milk_yield'], data_milkings['Milk_destination'])
    
    v12 = func.num_day_lactation_0_100(data_feed['Days In Milk'])
    v13 = func.num_day_lactation_101_200(data_feed['Days In Milk'])
    v14 = func.num_day_lactation_201_up(data_milkings['Animal_ID'], data_milkings['Milk_yield'], data_identity['Animal Number'], 
        data_identity['Official Reg. No. (ORN)'], data_feed['Official Reg. No. (ORN)'], data_feed['Days In Milk'])
    
    v15 = func.avg_milking_volume_lact_0_100(data_milkings['Date'], data_milkings['Animal_ID'], data_milkings['Action'], 
        data_milkings['Milk_yield'], data_identity['Animal Number'], data_identity['Official Reg. No. (ORN)'], 
        data_feed['Official Reg. No. (ORN)'], data_feed['Days In Milk'])
    v16 = func.avg_milking_volume_lact_101_200(data_milkings['Date'], data_milkings['Animal_ID'], data_milkings['Action'], 
        data_milkings['Milk_yield'], data_identity['Animal Number'], data_identity['Official Reg. No. (ORN)'], 
        data_feed['Official Reg. No. (ORN)'], data_feed['Days In Milk'])
    v17 = func.avg_milking_volume_lact_201_up(data_milkings['Date'], data_milkings['Animal_ID'], data_milkings['Action'], 
        data_milkings['Milk_yield'], data_identity['Animal Number'], data_identity['Official Reg. No. (ORN)'], 
        data_feed['Official Reg. No. (ORN)'], data_feed['Days In Milk'])


    # Append all key values to a DataFrame
    out_data = out_data.append({'Date': v0, 'avg_daily_milk_per_cow': v1, 'avg_daily_nr_of_milkings_per_cow': v2, 
        'nr_of_milkings_cows_yesterday': v3, 'avg_milk_from_vms_1': v4, 'avg_milk_from_vms_2': v5,
        'avg_milk_from_vms_1_and_2': v6, 'avg_nr_pass_smartgate': v7, 'projected_monthly_milk': v8,
        'avg_nr_of_kickOffs': v9,'avg_time_in_robot': v10,'Milk_to_tank_yesterday': v11,'cows_lactation_day_0-100': v12,
        'cows_lactation_day_101-200': v13,'cows_lactation_day_201-': v14,'avg_milking_volume_lact_0-100': v15,
        'avg_milking_volume_lact_101-200': v16, 'avg_milking_volume_lact_201-': v17}, ignore_index = True)

# Write key values to a csv file
out_data.to_csv("keyvalues.csv", index=False)
out_data.to_csv("keyvaluesOverView.csv", index=False, sep = ';')

stat = func.cow_stat_kickoffs(data_milkings['Date'], data_milkings['Animal_ID'], data_milkings['Milk_duration'], 
    data_milkings['Action'], data_milkings['Milk_yield'], data_milkings['Nr_of_kickOffs'], data_identity['Animal Number'],
    data_identity['Official Reg. No. (ORN)'], data_feed['Official Reg. No. (ORN)'], data_feed['Days In Milk'])
(stat[stat['Nr_of_kickOffs']>2]).to_csv("kickOffs.csv", index=False)

stat_milking_once_below_thresh = func.milking_once_below_thresh(data_cow['Date'], data_cow['Animal_ID'], data_cow['Total_milk_yield'], data_cow['Nr_of_milkings'], 20)
stat_milking_more_below_thresh = func.milking_more_below_thresh(data_cow['Date'], data_cow['Animal_ID'], data_cow['Total_milk_yield'], data_cow['Nr_of_milkings'], 25)

stat_milking_once_below_thresh.to_csv("stat_milking_once_below_thresh.csv", index=False)
stat_milking_more_below_thresh.to_csv("stat_milking_more_below_thresh.csv", index=False)
