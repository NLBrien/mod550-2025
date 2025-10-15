# -------- INFO --------
"""
Repository: https://github.com/NLBrien/mod550-2025
Creation date: 2025-10-13
Author: Nathan L.Brien
Course: MOD550 - Machine Learning
Title: Semester project
Description: Linear Regression in simple Python (NumPy and sklearn)

Last modification date: 2025-10-14
"""

# -------- LIBRARIES --------

import numpy as np
from sklearn.linear_model import LinearRegression

# -------- LINEAR REGRESSION --------
"""
Linear Regression in simple Python (NumPy and sklearn)

Before using this function, ensure that:
    - The necessary library is imported (NumPy, sklearn)
    - The data is numeric
    - The data contains no NaN values
Parameters:
    LinReg_x : [array], feature data (1D or 2D)
    LinReg_y : [array], target data
Returns:
    LinReg_model.coef_: [ndarray], regression coefficients
    LinReg_model.intercept_: [float], intercept term
    LinReg_y_pred : [ndarray], predicted values
"""

def Linear_Regression(LinReg_x, LinReg_y):

    ## Assign arrays
    x = np.array(LinReg_x, dtype=float)
    y = np.array(LinReg_y, dtype=float)

    # Reshape "x" if data 1D instead of 2D
    if x.ndim == 1:
        x = x.reshape(-1, 1)

    # Initialize linear regresison model
    LinReg_model = LinearRegression()

    # Fit the model with the data
    LinReg_model.fit(x, y)

    # Predictions
    LinReg_y_pred = LinReg_model.predict(x)

    return LinReg_model.coef_, LinReg_model.intercept_, LinReg_y_pred, LinReg_model

# -------- FUNCTION CALLBACK EXAMPLE --------

"""
# Define linear regression data
LinReg_x = [1, 2, 3, 4, 5]
LinReg_y = [2, 4, 5, 4, 5]

# Callback and run linear regression function
coeffs, intercept, LinReg_y_pred, LinReg_model = Linear_Regression(LinReg_x, LinReg_y)

# Print results
print("Intercept:", intercept)
print("Coefficients:", coeffs)
print("Predictions:", LinReg_y_pred)
"""
