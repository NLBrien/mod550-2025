# INFO
"""
Repository: https://github.com/NLBrien/mod550-2025
Creation date: 2025-09-16
Author: Nathan L.Brien
Course: MOD550 - Machine Learning
Title: Semester project
Description: Clean and merge main datasets imported through MOD550-P1-NLB-datasets.py

Last modification date: 2025-10-12
"""

#----------------------------------------------------------------------

# LIBRARIES

import pandas as pd
import numpy as np
from MOD550_P1_NLB_datasets import (
    grfc_data,
    total_population_data,
    total_gdp_data,
    capita_gdp_data
)
"""
Import 1 = grfc_data
Import 2 = total_population_data
Import 3 = total_gdp_data
Import 4 = capita_gdp_data
"""

#----------------------------------------------------------------------

# DATA CLEANING

## For total_population_data, remove unnecessary columns and years from 1960 to 2015
total_population_data.drop(
    columns = ["Country Name", "Indicator Name", "Indicator Code", "Unnamed: 69"]
    + list(total_population_data.loc[:, "1960":"2015"].columns),
    inplace=True
)

## For total_gdp_data, remove unnecessary columns and years from 1960 to 2015
total_gdp_data.drop(
    columns = ["Country Name", "Indicator Name", "Indicator Code", "Unnamed: 69"]
    + list(total_gdp_data.loc[:, "1960":"2015"].columns),
    inplace=True
)

## For capita_gdp_data, remove unnecessary columns and years from 1960 to 2015
capita_gdp_data.drop(
    columns = ["Country Name", "Indicator Name", "Indicator Code", "Unnamed: 69"]
    + list(capita_gdp_data.loc[:, "1960":"2015"].columns),
    inplace=True
)

## For grfc_data, remove unnecessary columns that won't be used in analysis
grfc_data.drop(columns=[
    'GRFC edition',
    'Analysis period',
    'Selection in the GRFC',
    'Selection criteria',
    'Data availability', 'Source',
    'Population group/\nGeographical area analysed',
    'Methodology',
    'LOWER BOUND Population in Phase 3 or above #',
    'LOWER BOUND Population in Phase 3 or above %'
    ], 
    inplace=True
)

## For grfc_data, rename columns for merging
grfc_data.rename(
    columns={
        "ISO Code 3": "Country Code",
        "Year of reference": "Year"
    }, 
    inplace=True
)

## For grfc_data, replace empty or N/A values cell content with na_values=NaN
"""
Clean the grfc_data dataset has some inconsistencies in values
(visual check done through Excel file)
Turn the following data values into NaN:
    empty values
    "N/A"
    "merged Phases"
    "merged with Phase 2"
    "merged with Phase 3"
"""
grfc_data.replace([
    "",
    "-",
    "N/A",
    "merged Phases",
    "merged with Phase 2",
    "merged with Phase 3"
    ], 
    np.nan,
    inplace=True
)

#----------------------------------------------------------------------

# DATA RESHAPE
"""
Reshape datasets before merging to match main dataset grfc_data format
"""
## For total_population_data, reshape from years columns to population format (vertical)
total_population_vertical = total_population_data.melt(
    id_vars = "Country Code",
    var_name = "Year",
    value_name = "Total country population"
)

## For total_gdp_data, reshape from years columns to population format (vertical)
total_gdp_vertical = total_gdp_data.melt(
    id_vars = "Country Code",
    var_name = "Year",
    value_name = "Total country GDP (US$)"
)

## For capita_gdp_data, reshape from years columns to population format (vertical)
capita_gdp_vertical = capita_gdp_data.melt(
    id_vars = "Country Code",
    var_name = "Year",
    value_name = "GDP per capita (US$)"
)

#----------------------------------------------------------------------

# DATA SORTING
"""
Make sure all datasets are sorted by ISO3 country code and year (ascending)
"""

## For total_population_vertical, sort data from years first (ascending), then by country code (ascending)
total_population_vertical = total_population_vertical.sort_values(
    by=["Year", "Country Code"])

## For total_gdp_vertical, sort data from years first (ascending), then by country code (ascending)
total_gdp_vertical = total_gdp_vertical.sort_values(
    by=["Year", "Country Code"])

## For capita_gdp_vertical, sort data from years first (ascending), then by country code (ascending)
capita_gdp_vertical = capita_gdp_vertical.sort_values(
    by=["Year", "Country Code"])

## For grfc_data, sort data from years first (ascending), then by country code (ascending)
grfc_data = grfc_data.sort_values(by=["Year", "Country Code"])

#----------------------------------------------------------------------

# DATA TYPE CONVERSION
"""
Make sure all datasets have the same data types for merging

Use of AI for data value merge conflict debugging
Microsoft Copilot version 1.25091.124.0
"""
## For total_population_vertical, convert "Year" columns to numeric with error buffer
total_population_vertical["Year"] = pd.to_numeric(
    total_population_vertical["Year"],
    errors="coerce").astype("Int64")

## For total_gdp_vertical, convert "Year" columns to numeric with error buffer
total_gdp_vertical["Year"] = pd.to_numeric(
    total_gdp_vertical["Year"],
    errors="coerce").astype("Int64")

## For capita_gdp_vertical, convert "Year" columns to numeric with error buffer
capita_gdp_vertical["Year"] = pd.to_numeric(
    capita_gdp_vertical["Year"],
    errors="coerce").astype("Int64")

## For grfc_data, convert "Year" columns to numeric with error buffer
grfc_data["Year"] = pd.to_numeric(grfc_data["Year"], errors="coerce").astype("Int64")

#----------------------------------------------------------------------

# MERGE DATASETS
"""
Merge datasets into one main dataset
mod550_p1_nlb_data_merged = grfc_data + other datasets
"""
mod550_p1_nlb_data_merged = grfc_data.copy()

## Replace "Total country population" column with total_population_vertical
mod550_p1_nlb_data_merged.drop(columns = "Total country population", inplace=True)
mod550_p1_nlb_data_merged = mod550_p1_nlb_data_merged.merge(
    total_population_vertical,
    on=["Country Code", "Year"],
    how="left"
    )

## Add "Total country GDP" column from total_gdp_vertical
mod550_p1_nlb_data_merged = mod550_p1_nlb_data_merged.merge(
    total_gdp_vertical,
    on=["Country Code", "Year"],
    how="left"
    )

## Add "GDP per Capita" column from capita_gdp_vertical
mod550_p1_nlb_data_merged = mod550_p1_nlb_data_merged.merge(
    capita_gdp_vertical,
    on=["Country Code", "Year"],
    how="left"
    )

#----------------------------------------------------------------------

# EXPORT

## Export merged dataset to xlsx file (full path)
mod550_p1_nlb_data_merged.to_excel(
    r"C:\Users\natha\UiS - MOD550\mod550-2025\MOD550-P1-NLB-datasets\MOD550-P1-NLB-data_merged.xlsx",
    index=False
)

## Export merged dataset to csv file (full path)
mod550_p1_nlb_data_merged.to_csv(
    r"C:\Users\natha\UiS - MOD550\mod550-2025\MOD550-P1-NLB-datasets\MOD550-P1-NLB-data_merged.csv",
    index=False
)