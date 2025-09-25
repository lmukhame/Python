import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Reading csv file
power_consumption = pd.read_csv("Energy_consumption/household_power_consumption_2010.csv")

# Preprocessing
# Changing index to datetime type
power_consumption["DateTime"] = pd.to_datetime(power_consumption["Date"]+" "+power_consumption["Time"])
power_consumption = power_consumption.drop(columns=["Date", "Time"])
power_consumption = power_consumption.set_index("DateTime")

# Changing data type of columns to numeric values
power_consumption = power_consumption.apply(pd.to_numeric, errors='coerce')

# Handling missing values by linear interpolation
power_consumption = power_consumption.interpolate()

# Downsampling to hourly values
power_consumption_hourly = power_consumption.resample("h").mean()

# Vizualizing hourly power consumption
power_consumption_hourly["Global_active_power"].plot(figsize=(18,5), title = "Hourly Household Power Consumption")
plt.show()

# Feature engineering 
# Creating features like hour of the day, a day of the week and cheching if the day is weekend
power_consump_h_feature = power_consumption_hourly.copy()
power_consump_h_feature["Hour"] = power_consump_h_feature.index.hour
power_consump_h_feature["DayOfWeek"] = power_consump_h_feature.index.dayofweek
power_consump_h_feature["Is_Weekend"] = power_consump_h_feature["DayOfWeek"].apply(lambda x: 1 if x>=5 else 0) 

# Rolling statistics for 3 hours, 24 hours and 7 days
power_consump_h_feature["Rolling_mean_4h"] = power_consumption_hourly["Global_active_power"].rolling(window=4, center=True).mean()
power_consump_h_feature["Rolling_mean_24h"] = power_consumption_hourly["Global_active_power"].rolling(window=24, center=True).mean()
power_consump_h_feature["Rolling_mean_7d"] = power_consumption_hourly["Global_active_power"].rolling(window="7D", center=True).mean()
power_consump_h_feature["Rolling_std_4h"] = power_consumption_hourly["Global_active_power"].rolling(window=4, center=True).std()
power_consump_h_feature["Rolling_std_24h"] = power_consumption_hourly["Global_active_power"].rolling(window=24, center=True).std()
power_consump_h_feature["Rolling_std_7d"] = power_consumption_hourly["Global_active_power"].rolling(window="7D", center=True).std()

# Vizualizing rollling statistics and hourly power consumption
power_consump_h_feature[["Global_active_power", "Rolling_mean_4h", "Rolling_mean_24h", "Rolling_mean_7d", "Rolling_std_4h", "Rolling_std_24h", "Rolling_std_7d"]].plot(figsize=(18,5), title = "Hourly Household Power Consumption")
plt.xlabel("DateTime")
plt.ylabel("Power, kW")
plt.show()

# Calculating total load from sub_meterings
# power_consump_h_feature["Total_load"] = power_consump_h_feature[["Sub_metering_1","Sub_metering_2", "Sub_metering_3"]].sum(axis=1)

# Lagged Variables 
# Frequency Features
# Machine Learning Model
