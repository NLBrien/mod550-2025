# INFORMATION
"""
Repository: https://github.com/NLBrien/mod550-2025
Creation date: 2025-09-24
Author: Nathan L.Brien
Course: MOD550 - Machine Learning
Title: Semester project
Description: Assignment 1, data selection
    N.B.:   Data isolated from the dataset is the food crisis level (phase) per year per country:
                Phase 1:    None (Acceptable)
                Phase 2:    Stress (Alert)
                Phase 3:    Crisis (Serious)
                Phase 4:    Emergency (Critical)
                Phase 5:    Catastrophe (Vital)

Last modification date: 2025-09-24
"""

#----------------------------------------------------------------------

# LIBRARIES
import numpy as np
import pandas as pd

#----------------------------------------------------------------------

# FUNCTIONS

## Read XLSX file (Absolute file path)
#Script path: "C:\Users\natha\UiS - MOD550\mod550-2025\MOD550-NLB-TASK_1\MOD550-P1-NLB-crisis_phase_isolation.py"
#File path: C:\Users\natha\UiS - MOD550\mod550-2025\MOD550-P1-NLB-datasets\MOD550-P1-NLB-GRFC
grfc_data = pd.read_excel(
    r"C:\Users\natha\UiS - MOD550\mod550-2025\MOD550-P1-NLB-datasets\MOD550-P1-NLB-GRFC\grfc_afi_database_2016-2024.xlsx",
    sheet_name="GRFC 2025_AFI Master"
)

### Preview header list
print("Available columns:", grfc_data.columns.tolist())
### Preview first header and first row
print(grfc_data.head(1))

## Select data from dataset (filtering unnecessary columns)
"""
Keep the following columns list:
    ISO Code 3
    Countries/territories
    Region
    Year of reference
    Population group selected
    Population in Phase 1
    Population in Phase 2
    Population in Phase 3
    Population in Phase 4
    Population in Phase 5
"""
keep_columns = [
    "ISO Code 3",
    "Countries/territories",
    "Region",
    "Year of reference",
    "Population group selected",
    "Population in Phase 1 #",
    "Population in Phase 2 #",
    "Population in Phase 3 #",
    "Population in Phase 4 #",
    "Population in Phase 5 #",
]
grfc_data_phases = grfc_data[keep_columns].copy()

## Data cleaning and screening
"""
Turn the following data values into NaN:
    empty values
    "N/A"
    "merged Phases"
    "merged with Phase 2"
    "merged with Phase 3"
"""
grfc_data_phases = grfc_data_phases.replace(
    ["", "N/A", "merged Phases", "merged with Phase 2", "merged with Phase 3"], 
    np.nan
)

## Replace "Population in Phase [1-5]" with True/False
"""
To categorize whether or not a country is in a crisis phase regardless of the population
"""
phase_columns = [
    "Population in Phase 1 #",
    "Population in Phase 2 #",
    "Population in Phase 3 #",
    "Population in Phase 4 #",
    "Population in Phase 5 #",
]
for phase_bool in phase_columns:
    grfc_data_phases[phase_bool] = grfc_data_phases[phase_bool].apply(
        lambda x: True if pd.notna(x) and isinstance(x, (int, float)) and x > 0 else False
    )
    """
    Use of AI for phase boolean logic debugging
    Chat GPT version GPT-5 mini
    """

## Highest phase status override
"""
Only keep the highest food crisis phase active per country per year.
(e.g.: if Algeria has phase 3 crisis in 1990, set phase 2 and phase 1 as "False")
Find the highest phase marked as True, start from Phase 5 down to Phase 1 (reverse) since
dataset crisis phases are set from lowest to highest from left to right
"""
def highest_phase_override(row):
    for phase in reversed(phase_columns):  
        if row[phase]:
            for lower_phase in phase_columns:
                if lower_phase != phase:
                    row[lower_phase] = False
            break
    return row

grfc_data_phases = grfc_data_phases.apply(highest_phase_override, axis=1)

### Preview cleaned dataset
print(grfc_data_phases.head(10))

#----------------------------------------------------------------------

# EXPORT

## Export final result to CSV without index
grfc_data_phases.to_csv(
    r"C:\Users\natha\UiS - MOD550\mod550-2025\MOD550-P1-NLB-datasets\MOD550-P1-NLB-GRFC\phase_per_year.csv",
    index=False
)