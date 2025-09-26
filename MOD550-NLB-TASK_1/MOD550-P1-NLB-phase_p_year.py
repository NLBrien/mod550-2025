# INFORMATION
"""
Repository: https://github.com/NLBrien/mod550-2025
Creation date: 2025-09-24
Author: Nathan L.Brien
Course: MOD550 - Machine Learning
Title: Semester project
Description: Assignment 1, data selection
    N.B.:   Further filter and isolate data from the dataset of food crisis level (phase) per year:
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

## Read CSV file (Absolute file path)
#Script path: "C:\Users\natha\UiS - MOD550\mod550-2025\MOD550-NLB-TASK_1\MOD550-P1-NLB-phase_p_year.py"
#File path: "C:\Users\natha\UiS - MOD550\mod550-2025\MOD550-P1-NLB-datasets\MOD550-P1-NLB-GRFC\phase_per_year.csv"
grfc_count_per_phase = pd.read_csv(
    r"C:\Users\natha\UiS - MOD550\mod550-2025\MOD550-P1-NLB-datasets\MOD550-P1-NLB-GRFC\phase_per_year.csv"
)

### Preview header list
print("Available columns:", grfc_count_per_phase.columns.tolist())
### Preview first header and first row
print(grfc_count_per_phase.head(1))

## Select data from dataset (filtering unnecessary columns)
"""
From previously narrowed down dataset (grfc_data_phases in MOD550-P1-NLB-crisis_phase_isolation)
Select only crisis phase per country per year
"""
phase_columns = [
    "Population in Phase 1 #",
    "Population in Phase 2 #",
    "Population in Phase 3 #",
    "Population in Phase 4 #",
    "Population in Phase 5 #",
]

keep_columns = [
    "Year of reference",
] + phase_columns

### Copy result to new dataset
grfc_nphase_per_year = grfc_count_per_phase[keep_columns].copy()

## Data merge and structure
"""
Turn the remaining data into list of list as 3d points
    x_year: year of reference
    y_phase: value transposed as follows;
        Population in Phase 1 # => y = 1
        Population in Phase 2 # => y = 2
        Population in Phase 3 # => y = 3
        Population in Phase 4 # => y = 4
        Population in Phase 5 # => y = 5
    z_number: total number of occurence (countries) in the respective Population Phase
"""
### Create empty 3D point list: [year, phase_number, count]
grfc_phase_3d_points = []

### Stack data from phases column for each year
for year, group in grfc_count_per_phase.groupby("Year of reference"):
    # Groupby function call required for counting iterations
    for phase, phase_count in enumerate(phase_columns, start=1):  
        # Use of enumerate function to rename columns to level (Phase 1 = y=1, ..., Phase 5 = y=5)
        count = group[phase_count].apply(lambda x: pd.notna(x) and x > 0).sum()
        # Use of count function to sum the number of rows where the population is "True"
        """
        Use of AI for phase count sum logic debugging
        Chat GPT version GPT-5 mini
        """
        year_int = int(year)
        phase_int = int(phase)
        count_int = int(count)
        # force integer type on 3d points variables
        grfc_phase_3d_points.append([year_int, phase_int, count_int])

# Convert 3D point list to DataFrame
grfc_phase_3d_points = pd.DataFrame(grfc_phase_3d_points, columns=["Year", "Phase", "Count"])

### Preview year list
print(grfc_phase_3d_points["Year"])
### Preview final 3D structured dataset
print(grfc_phase_3d_points.head(10))

#----------------------------------------------------------------------

# EXPORT

## Export final result to CSV with index
grfc_phase_3d_points.to_csv(
    r"C:\Users\natha\UiS - MOD550\mod550-2025\MOD550-NLB-TASK_1\grfc_phase_3d_points.csv"
)