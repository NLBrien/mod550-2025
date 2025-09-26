# INFORMATION
"""
Repository: https://github.com/NLBrien/mod550-2025
Creation date: 2025-09-23
Author: Nathan L.Brien
Course: MOD550 - Machine Learning
Title: Random distribution 2d
Description: Function for callback, 2d list random generation

Last modification date: 2025-09-23
"""

#----------------------------------------------------------------------

# LIBRARIES
import random

#----------------------------------------------------------------------

# FUNCTION
class RAND_POINTS_2D:
    def __init__(self, n_rand_2d, x_rand_2d_min=0, x_rand_2d_max=0, y_rand_2d_min=0, y_rand_2d_max=0):
        """
        Initialization of the random 2d points generator function
        Inputs:
            n_rand_2d: number of random 2d points to generate
            x_rand_2d_min; lower limit for x values
            x_rand_2d_max: upper limit for x values
            y_rand_2d_min: lower limit for y values
            y_rand_2d_max: upper limit for y values
        Outputs:
            RAND_GEN_2D function return
        """
        self.n_rand_2d = n_rand_2d
        self.x_rand_2d_min = x_rand_2d_min
        self.x_rand_2d_max = x_rand_2d_max
        self.y_rand_2d_min = y_rand_2d_min
        self.y_rand_2d_max = y_rand_2d_max

    def RAND_GEN_2D(self):
        """
        Generate a list of random 2D points
        Inputs:
            RAND_POINTS_2D __init__ inputs
        Outputs:
            List (n_rand_2d number) of tuples (2d points coordinates): [(x_1, y_1), (x_2, y_2), ..., (x_n, y_n)]
        """
        rand_2d_points = [
            (random.uniform(self.x_rand_2d_min, self.x_rand_2d_max),
             random.uniform(self.y_rand_2d_min, self.y_rand_2d_max))
            for _ in range(self.n_rand_2d)
        ]
        
        return rand_2d_points

#----------------------------------------------------------------------

# CALLBACK SEQUENCE
"""
# Import the class function to your codes
from Random_distribution_2d import RAND_POINTS_2D

# Assign a name to the class function
"__name__" = RAND_POINTS_2D(
    n_rand_2d=5,
    x_rand_2d_min=0, x_rand_2d_max=10,
    y_rand_2d_min=0, y_rand_2d_max=10,
)

# Call the method to generate points
"__result__" = "__name__".RAND_GEN_2D()

# Print the result
print("__result__")
"""