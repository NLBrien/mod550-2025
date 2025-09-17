# *INFO*
"""
Repository: https://github.com/NLBrien/mod550-2025
Creation date: 2025-09-16
Author: Nathan L.Brien
Course: MOD550 - Machine Learning
Title: Semester project
Description: 

Last modification date: 2025-09-16
"""

#----------------------------------------------------------------------

# *LIBRARIES*
import pandas as pd
import numpy as no
import MOD550-P1-NLB-datasets

#----------------------------------------------------------------------

# *DATA MODIFICATIONS*
"""
1- for total_population_data, remove columns from 1960 to 2016
2- for total_gdp_data, remove columns from 1960 to 2016
3- for capita_gdp_data, remove colomns from 1960 to 2016
4- for grfc_data, validate years 2017 to 2024 for each country row (make sure everything from 2016 to 2024 is there)
5- for grfc_data, replace all ["N/A", "-"] cell content with na_values=None
"""
## 1
total_population_data.drop(columns=["1960":"2016"])

## 2
total_gdp_data.drop(columns=["1960":"2016"])

## 3
capita_gdp_data.drop(columns=["1960":"2016"])

## 4
required_years = set(range(2016, 2025))  # 2016 to 2024 inclusive
missing_years_per_country = {}

for country, group in grfc_data.groupby(ISO3):
    years_present = set(group["year of reference"].unique())
    missing = required_years - years_present
    if missing:
        missing_years_per_country[country] = sorted(missing)

## 5
grfc_data(na_values=["N/A", "-"])

#----------------------------------------------------------------------

# *MERGE*
"""
mod550_p1_nlb_data_merged = grfc_data
1- for mod550_p1_nlb_data_merged, replace total country population column with total_population_data
2- for mod550_p1_nlb_data_merged, add total gdp column from total_gdp_data
3- for mod550_p1_nlb_data_merged, add gdp per capita from capita_gdp_data
"""
mod550_p1_nlb_data_merged = grfc_data
## 1
total_population_data.sort(ISO3)
mod550_p1_nlb_data_merged
## 2
total_gdp_data.sort(ISO3)
mod550_p1_nlb_data_merged
## 3
capita_gdp_data.sort(ISO3)
mod550_p1_nlb_data_merged

#----------------------------------------------------------------------

# *EXPORT*
## Export merged dataset to xlsx file (Relative path to this script)
mod550_p1_nlb_data_merged.to_excel("MOD550-P1-NLB-data_merged.xlsx", index=False)
## Export merged dataset to csv file (Relative path to this script)
mod550_p1_nlb_data_merged.to_csv("MOD550-P1-NLB-data_merged.csv", index=False)