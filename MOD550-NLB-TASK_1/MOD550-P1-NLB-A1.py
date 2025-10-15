# *INFO*
"""
Repository: https://github.com/NLBrien/mod550-2025
Creation date: 2025-09-16
Author: Nathan L.Brien
Course: MOD550 - Machine Learning
Title: Semester project
Description: Assignment 1, data visualization
    N.B.:   as the main dataset merging hasn't been completed, i only used total_gdp_data,
            details of selected dataset can be found in MOD550-P1-NLB-datasets

Last modification date: 2025-09-16
"""

#----------------------------------------------------------------------

# *LIBRARIES*
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#----------------------------------------------------------------------

# *FUNCTIONS*
## import selected csv file data
total_gdp_data = pd.read_csv("MOD550-P1-NLB-datasets/MOD550-P1-NLB-GDP_total/API_NY.GDP.MKTP.CD_DS2_en_csv_v2_661854.csv", skiprows=4)

## remove columns from 1960 to 2015
total_gdp_data = total_gdp_data.drop(columns=[str(year) for year in range(1960, 2017)])

## add a total gdp column (cumulated GDP per country between 2016 to 2024)
total_gdp_data['Total_GDP_2016_2024'] = total_gdp_data.loc[:, '2016':'2024'].sum(axis=1, skipna=True)

## call describe function to obtain data calculation [count, mean, std, min, 25%, 50%, 75%, max]
total_gdp_data.describe()

## Create histogram
total_gdp_data["Country"].hist()
plt.xlabel("Country")
plt.ylabel("Total GDP ($USD)")
plt.title("Total GDP cumulated per country between 2016 to 2024")
plt.show()

## Create heatmap
plt.figure()
sns.heatmap(total_gdp_data, annot=True, cmap="YlGnBu")  # annot=True shows values in cells
plt.title("Example Heatmap")
plt.show()
