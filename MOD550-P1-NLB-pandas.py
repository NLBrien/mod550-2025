# *INFO*
"""
Repository: https://github.com/NLBrien/mod550-2025
Date: 2025-09-16
Author: Nathan L.Brien
Course: MOD550 - Machine Learning
Title: Semester project
Description: Importing pandas and its optional dependencies

Last modification date: 2025-09-16
"""

#----------------------------------------------------------------------

# *PADAS SETUP*
"""
All commands were run separatly on the local machine terminal (C:\Users\natha) through VSCode
"""

## Pandas installation
"""
Pandas module installation => data analysis and manipulation library for Python
"""
#pip install pandas

## Performance optional pandas dependencies
"""
numexpr => accelerates certain numerical operations
bottleneck => accelerates certain types of nan reductions
numba => alternative execution engine for operations that accept engine="numba" argument
"""
#pip install "pandas[performance]"

## Visual formatting optional pandas dependencies
"""
matplotlib => plotting library
Jinja2 => conditional formatting with DataFrame.style
tabulate => printing in Markdown-friendly format (see tabulate)
"""
#pip install "pandas[plot, output-formatting]"

## Computation optional pandas dependencies
"""
SciPy => miscellaneous statistical functions
xarray => pandas-like API for N-dimensional data
"""
#pip install "pandas[computation]"


## Excel optional pandas dependencies
"""
xlrd => reading Excel
xlsxwriter => writing Excel
openpyxl => reading / writing for xlsx files
pyxlsb => reading for xlsb files
python-calamine => reading for xls/xlsx/xlsb/ods files
"""
#pip install "pandas[excel]"
