# *INFO*
"""
Repository: https://github.com/NLBrien/mod550-2025
Date: 2025-09-11
Author: Nathan L.Brien
Course: MOD550 - Machine Learning
Title: Semester project
Description: importing project main datasets with pandas

Last modification date: 2025-09-16
"""

#----------------------------------------------------------------------

# *LIBRARIES*
import pandas as pd

#----------------------------------------------------------------------

# *IMPORTS*

## grfc - Global Report on Food Crises (GRFC)
"""
Data source: Humanitarian Data Exchange (HDX) and Food Security Information Network (FSIN)
Data link: https://data.humdata.org/dataset/fsin-grfc
Data description: Food insecurity level per country per year, from 2016 to 2024
Data format: CSV and XLSX
Data columns:
    - ISO Code 3: ISO 3-letter country code
    - Country/territories: Name of the country
    - Region: Geographical region classification
    - GRFC edition: GRFC publication year
    - Year of reference: original data year of reference
    - Selection in the GRFC: wether or not to be included in the report [Y(yes), N(no)]
    - Selection criteria: reason of inclusion to report
    - Population group selected: which part of the population has been studied
    - Data availaility: wether or not there is accessibility to data for report [Y(yes), N(no)]
    - Source: data source
    - Pupulation group/ Geographical area analysed:
    - Methodology:
        - IPC → Global classification scale for food insecurity.
        - ENA → Rapid nutrition survey method.
        - CARI → WFPs household food security scoring system.
        - FEWS NET → Early warning and forecasting network that often uses IPC.
    - Total country population: number of human individuals living on the territory during that year
    - Population analysed: number of human individuals selected for the report
    - % pop analysed of tot country pop: share of population analysed of total country population (%)
    - Analysis period: time interval for the report analysis
    - Population in Phase 1 #: population in food crisis category classification number 1 [None (Acceptable)]
    - Population  in Phase 1 %: share population in food crisis category classification 1 [None (Acceptable)]
    - Population in Phase 2 #: population in food crisis category classification number 2 [Stress (Alert)]
    - Population  in Phase 2 %: share population in food crisis category classification 2 [Stress (Alert)]
    - Population in Phase 3 #: population in food crisis category classification number 3 [Crisis (Serious)]
    - Population  in Phase 3 %: share population in food crisis category classification 3 [Crisis (Serious)]
    - Population in Phase 4 #: population in food crisis category classification number 4 [Emergency (Critical)]
    - Population in Phase 4 %: share population in food crisis category classification 4 [Emergency (Critical)]
    - Population Phase 5 #: population in food crisis category classification number 5 [Catastrophe (Vital)]
    - Population Phase 5 %: share population in food crisis category classification 5 [Catastrophe (Vital)]
    - Population in Phase 3 or above #: population in food crisis category classification 3 and higher
    - Population in Phase 3 or above %: share population in food crisis category classification 3 and higher
    - Major food  crisis (Y/N): wether or not the country is considered to be in a major food crisis
    - Primary driver: element that is considered to be the main reason of food crisis
    - Secondary drive: element that is considered to be the second reason of food crisis
    - Tertiary driver: element that is considered to be the third reason of food crisis
"""
# Read CSV file (Relative path to this script)
grfc_metadata = pd.read_csv("MOD550-P1-NLB-datasets/MOD550-P1-NLB-GRFC/metadata-fsin-grfc.csv")
# Read XLSX file (Relative path to this script)
grfc_data = pd.read_excel("MOD550-P1-NLB-datasets/MOD550-P1-NLB-GRFC/grfc_afi_database_2016-2024.xlsx",
                          sheet_name="GRFC 2025_AFI Master")
# Preview metadata headers
grfc_data.head(5)

## total_population - Total population per country
"""
Data source: World Bank Group
Data link: https://data.worldbank.org/indicator/SP.POP.TOTL
Data description: Total population per country per year, from 1960 to 2024
Data format: CSV
Metadata columns:
    - Country Code: ISO 3-letter country code
    - Region: Geographical region classification
    - IncomeGroup: Income group classification
    - SpecialNotes: Additional notes about the country
    - TableName: Name of the country
Data columns:
    - Country Name: Name of the country
    - Country Code: ISO 3-letter country code
    - Indicator Code: "SP.POP.TOTL"
    - Indicator: Year of the data point
Data values:
    - Population: Total population for the country in that year
"""
# Read CSV files (Relative path to this script)
total_population_metadata_cntry = pd.read_csv("MOD550-P1-NLB-datasets/MOD550-P1-NLB-population_total/Metadata_Country_API_SP.POP.TOTL_DS2_en_CSV_v2_661867.csv")
total_population_metadata_indic = pd.read_csv("MOD550-P1-NLB-datasets/MOD550-P1-NLB-population_total/Metadata_Indicator_API_SP.POP.TOTL_DS2_en_CSV_v2_661867.csv")
total_population_data = pd.read_csv("MOD550-P1-NLB-datasets/MOD550-P1-NLB-population_total/API_SP.POP.TOTL_DS2_en_CSV_v2_661867.csv")
# Preview metadata headers
total_population_data.head(5)

## total_gdp - Total GDP per country
"""
Data source: World Bank Group
Data link: https://data.worldbank.org/indicator/NY.GDP.MKTP.CD
Data description: Total GDP per country per year, from 1960 to 2024
Data format: CSV
Metadata columns:
    - Country Code: ISO 3-letter country code
    - Region: Geographical region classification
    - IncomeGroup: Income group classification
    - SpecialNotes: Additional notes about the country
    - TableName: Name of the country
Data columns:
    - Country Name: Name of the country
    - Country Code: ISO 3-letter country code
    - Indicator Name: "GDP (current US$)"
    - Indicator Code: "NY.GDP.MKTP.CD"
    - Indicator: Year of the data point
Data values:
    - GDP: Total GDP for the country in that year
"""
# Read CSV files (Relative path to this script)
total_gdp_cntry_metadata = pd.read_csv("MOD550-P1-NLB-datasets/MOD550-P1-NLB-GDP_total/Metadata_Country_API_NY.GDP.MKTP.CD_DS2_en_csv_v2_661854.csv")
total_gdp_indic_metadata = pd.read_csv("MOD550-P1-NLB-datasets/MOD550-P1-NLB-GDP_total/Metadata_Indicator_API_NY.GDP.MKTP.CD_DS2_en_csv_v2_661854.csv")
total_gdp_data = pd.read_csv("MOD550-P1-NLB-datasets/MOD550-P1-NLB-GDP_total/API_NY.GDP.MKTP.CD_DS2_en_csv_v2_661854.csv")
# Preview metadata headers
total_gdp_data.head(5)

## capita_gdp - GDP per capita (person) per country
"""
Data source: World Bank Group
Data link: https://data.worldbank.org/indicator/NY.GDP.PCAP.CD
Data description: GDP per capita per country per year, from 1960 to 2024
Data format: CSV
Metadata columns:
    - Country Code: ISO 3-letter country code
    - Region: Geographical region classification
    - IncomeGroup: Income group classification
    - SpecialNotes: Additional notes about the country
    - TableName: Name of the country
Data columns:
    - Country Name: Name of the country
    - Country Code: ISO 3-letter country code
    - Indicator Name: "GDP per capita (current US$)"
    - Indicator Code: "NY.GDP.PCAP.CD"
    - Indicator: Year of the data point
Data values:
    - GDPPCAP: GDP per capita (person) for the country in that year
"""
# Read CSV files (Relative path to this script)
capita_gdp_metadata_cntry = pd.read_csv("MOD550-P1-NLB-datasets/MOD550-P1-NLB-GDP_capita/Metadata_Country_API_NY.GDP.PCAP.CD_DS2_en_csv_v2_661849.csv")
capita_gdp_metadata_indic = pd.read_csv("MOD550-P1-NLB-datasets/MOD550-P1-NLB-GDP_capita/Metadata_Indicator_API_NY.GDP.PCAP.CD_DS2_en_csv_v2_661849.csv")
capita_gdp_data = pd.read_csv("MOD550-P1-NLB-datasets/MOD550-P1-NLB-GDP_capita/API_NY.GDP.PCAP.CD_DS2_en_csv_v2_661849.csv")
# Preview metadata headers
capita_gdp_data.head(5)
