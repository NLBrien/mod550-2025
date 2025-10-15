# -------- INFO --------
"""
Repository: https://github.com/NLBrien/mod550-2025
Creation date: 2025-10-13
Author: Nathan L.Brien
Course: MOD550 - Machine Learning
Title: Semester project
Description: Neural network using keras and tensorflow

Last modification date: 2025-10-14
"""

# -------- LIBRARIES --------

import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.regularizers import l1, l2, l1_l2

# -------- NEURAL NETWORK --------
"""
Neural Network in simple Python using Keras

Before using this function, ensure that:
    - The necessary libraries are imported (NumPy, TensorFlow/Keras)
    - The input data is preprocessed and scaled (StandardScaler)
    - The data is numeric
    - The data contains no NaN values
Parameters:
    NN_X : [array], Feature data (1D or 2D)
    NN_y : [array], Target data
    dense_1: [int], (8, 16, 64, 128), Number of neurons for layer 1 (default = 8)
    dense_2: [int], (8, 16, 64, 128), Number of neurons for layer 2 (default = 64)
    activate_fnc: [str], ("relu", "tanh", "sigmoid", "elu"), Activating function for regression output (default = "relu")
    kernel_reg: [import], (l1, l2, l1_l2), Regularizing function for training (default = l2(0.01))
    optimize_fnc: [str], ("SGD", "Adagrad", "RMSProp", "Adam", "AdamW", "Nadam", "Adadelta")
        Optimizing function strategy, a.k.a. algorithm (default = "adam")
    epochs_nb : [int], Number of training epochs (default = 20)
Returns:
    NN_model : The trained neural network model
    NN_y_pred : [ndarray], Predicted values for the input X
"""
def Neural_Network(NN_x,
                   NN_y,
                   dense_1 = 8,
                   dense_2 = 64,
                   activate_fnc = "relu",
                   kernel_reg = l2(0.01),
                   optimize_fnc = "adam",
                   epochs_nb = 20, 
                   ):
    # Turn input values to numpy arrays
    NN_x = np.array(NN_x, dtype=float)
    NN_y = np.array(NN_y, dtype=float)

    # Reshape "y" if data 1D instead of 2D
    if NN_y.ndim == 1:
        NN_y = NN_y.reshape(-1, 1)

    # Define neural network model for linear regression
    NN_model = Sequential([
        Dense(dense_1, input_dim = 1, activation = activate_fnc, kernel_regularizer = kernel_reg),
        Dense(dense_2, activation = activate_fnc, kernel_regularizer = kernel_reg),
        Dense(1)
    ])

    # Complete the model
    NN_model.compile(optimizer = optimize_fnc, loss = "mse")

    # Train the model
    NN_model.fit(NN_x, NN_y, epochs = epochs_nb, verbose = 1)

    # Use the model for prediction
    NN_y_pred = NN_model.predict(NN_x)

    return NN_model, NN_y_pred

# -------- FUNCTION CALLBACK EXAMPLE --------

"""
# Define NN data
NN_x = [1, 2, 3, 4, 5]
NN_y = [2, 4, 5, 4, 5]

# Callback and run NN function
NN_model, NN_y_pred = Neural_Network(NN_x,
                                    NN_y,
                                    dense_1 = 8,
                                    dense_2 = 64,
                                    activate_fnc = "relu",
                                    optimize_fnc = "adam",
                                    kernel_reg = l2(0.01),
                                    epochs_nb = 20,
                                    )

# Print results
print("Neural Network preditions:", NN_y_pred)
"""
