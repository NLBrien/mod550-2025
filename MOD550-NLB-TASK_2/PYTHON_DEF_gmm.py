# -------- INFO --------
"""
Repository: https://github.com/NLBrien/mod550-2025
Creation date: 2025-10-14
Author: Nathan L.Brien
Course: MOD550 - Machine Learning
Title: Semester project
Description: Gaussian Mixture Model (GMM) in simple Python using sklearn

Last modification date: 2025-10-14
"""
# -------- LIBRARIES --------

import numpy as np
from sklearn.mixture import GaussianMixture

# -------- GMM --------
"""
Gaussian Mixture Model (GMM) in simple Python using sklearn

Before using this function, ensure that:
    - The necessary libraries are imported (NumPy, sklearn)
    - The input data is numeric
    - The data contains no NaN values
Parameters:
    GMM_x : [array], Feature data (1D or 2D)
    GMM_y : [array], Optional second feature dimension (1D or 2D)
    component_nb : [int], Number of Gaussian components (clusters) to fit (default = 2)
    RSEED : [int], Random seed for reproducibility (default = 42)
Returns:
    GMM_labels : [ndarray], cluster assignment for each point
    GMM_probs : [ndarray], soft probabilities of belonging to each cluster
    GMM_means : [ndarray], estimated Gaussian means
    GMM_covariances : [ndarray], covariance matrices of each Gaussian component
    GMM_model : [GaussianMixture object], the trained GMM model
"""
def Gaussian_Mixture_Model(GMM_x, component_nb = 2, RSEED = 42):
    
    # Turn input values to numpy arrays
    GMM_x = np.array(GMM_x, dtype=float)
    
    # Reshape "x" if data 1D instead of 2D
    if GMM_x.ndim == 1:
        GMM_x = GMM_x.reshape(-1, 1)

    # Initialize and fit Gaussian Mixture Model
    gmm = GaussianMixture(n_components = component_nb, random_state=RSEED)
    gmm.fit(GMM_x)

    # Predict hard labels and soft probabilities
    labels = gmm.predict(GMM_x)
    probs = gmm.predict_proba(GMM_x)

    return labels, probs, gmm.means_, gmm.covariances_, gmm

# -------- FUNCTION CALLBACK EXAMPLE --------

"""
# Define clustering data
GMM_x = [1, 2, 3, 10, 11, 12]
GMM_y = [1, 2, 1, 10, 11, 10]

# Callback and run GMM function
GMM_labels, GMM_probs, GMM_means, GMM_covs, GMM_model = Gaussian_Mixture_Model(GMM_x, GMM_y, n_components=2, RSEED=42)

# Print results
print("Cluster labels:", GMM_labels)
print("Soft probabilities:", GMM_probs)
print("Cluster means:", GMM_means)
print("Covariance matrices:", GMM_covs)
"""
