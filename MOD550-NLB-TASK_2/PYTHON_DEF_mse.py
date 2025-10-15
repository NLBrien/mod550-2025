# -------- INFO --------
"""
Repository: https://github.com/NLBrien/mod550-2025
Creation date: 2025-10-13
Author: Nathan L.Brien
Course: MOD550 - Machine Learning
Title: Semester project
Description: Mean squared error (mse) in vanilla Python

Last modification date: 2025-10-13
"""

# -------- LIBRARIES --------

## No external libraries needed

# -------- MSE --------
"""
Mean squared error (MSE) in vanilla Python

Before using this function, ensure that:
    - The data is numeric (int or float)
    - The two input lists have the same length
    - The data contains no NaN values
Parameters:
    mse_observed = [list], observed values
    mse_predicted = [list], predicted values
Returns:
    mse = [float], mean squared error between observed and predicted values
"""

def Mean_Squared_Error(mse_observed, mse_predicted):
   
	## Validate input lengths
    if len(mse_observed) != len(mse_predicted):
        raise ValueError(
            f"The lengths of input lists are not equal: "
            f"{len(mse_observed)} vs {len(mse_predicted)}"
        )

    ## Initialize sum of squared errors
    sum_square_error = 0

    ## Loop through observations
    for obs, pred in zip(mse_observed, mse_predicted):
        sum_square_error += (obs - pred) ** 2

    ## Calculate mean squared error
    mse = sum_square_error / len(mse_observed)

    return mse

# -------- FUNCTION CALLBACK EXAMPLE --------

"""
# Run linear regression first to get predictions
To use this function, first run Linear_Regression from PYTHON_DEF_linearregression.py to get predictions.

# Define mse data
mse_observed = LinReg_y
mse_predicted = LinReg_y_pred

# Callback and run mse function
mse = Mean_Squared_Error(mse_observed, mse_predicted)

# Print results
print("MSE:", mse)
"""
