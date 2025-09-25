# Mini-Project: Anomaly Detection in Houshold Power Consumption
This repository contains Python mini-project that implements **anomaly detection pipeline** on household power consumption.
The dataset for the project is taken from UCI Machine Learning Repository (https://archive.ics.uci.edu/ml/datasets/individual+household+electric+power+consumption) and contains **1-minute sampled measurements** from 2006–2010 for a single household. For the purpose of the project and to limit the storage usage, the dataset was filtered for 2010.

### Goal
1. Data preprocessing and vizualization
2. Feauture engineering nessesary for anomaly detection
3. Exploration of the effect of different feature engineering techniques 
4. Implementation of machine learning anomaly detection methods
5. Evoluation and comparison of methods
6. Vizualizaion of results and reporting in README file.

## Dataset Description
The records correspons to one-minute measurements.
Columns and varable information:
1. *Date*: Date in format dd/mm/yyyy
2. *Time*: time in format hh:mm:ss
3. *Global_active_power*: household global minute-averaged active power (in kilowatt)
4. *Global_reactive_power*: household global minute-averaged reactive power (in kilowatt)
5. *Voltage*: minute-averaged voltage (in volt)
6. *Global_intensity*: household global minute-averaged current intensity (in ampere)
7. *Sub_metering_1*: energy sub-metering No. 1 (in watt-hour of active energy). It corresponds to the kitchen, containing mainly a dishwasher, an oven and a microwave (hot plates are not electric but gas powered).
8. *Sub_metering_2*: energy sub-metering No. 2 (in watt-hour of active energy). It corresponds to the laundry room, containing a washing-machine, a tumble-drier, a refrigerator and a light.
9. *Sub_metering_3*: energy sub-metering No. 3 (in watt-hour of active energy). It corresponds to an electric water-heater and an air-conditioner.

## 1. Data Preprocessing 
- Loaded dataset (csv file) as a pandas DataFrame.
- Merged "Date" and "Time" columns into datetime format and seet it as index.
- Converted numerical colums to correct datatype.
- Used linear interpolation for handling missibng values.
- Downsampled the data form 1-minute to hourly data.
 
### Vizualization
Plot of time-series for an hourly power consumption.

## 2. Feature Engineering 
- Added derived **time-based features**: an hour of the day, a day of the week, weekend checker 
- Calculated **rolling statistics**: 
    -- *rolling average* (to capture trends) 
    -- *rolling standard deviation* (to measure dispersion of the data within time window)
*Time windows* of 4 hours, 24 hours are 7 days were implemented to capture the trends of daily and weekly power cycles, as well as 4 hours as a comparative trend to avoid oversmoothing. 

### Vizualization
Plot of time-series for an hourly power consumption with rolling statistics.

## Next Steps
2. Feature engineering: lagged variables
3. Machine learning models
4. Evaluation and vizualization

## Required Installations:
Installation of the following packages:
- Pandas
- Matplotlib (Pyplot)