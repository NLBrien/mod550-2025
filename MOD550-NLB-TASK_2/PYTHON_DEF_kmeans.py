# -------- INFO --------
"""
Repository: https://github.com/NLBrien/mod550-2025
Creation date: 2025-10-13
Author: Nathan L.Brien
Course: MOD550 - Machine Learning
Title: Semester project
Description:    Coefficient mean (k-means) visualization and running code
                in simple Python using sklearn

Last modification date: 2025-10-14
"""

# -------- LIBRARIES --------

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# -------- K MEANS --------
"""
K-Means clustering in simple Python using sklearn

Before using this function, ensure that:
    - The necessary libraries are imported (NumPy, scikit-learn, matplotlib for visualization)
    - The input data is numeric
    - The data contains no NaN values
K_Means_Elbow:
    Parameters:
        KM_x : [array], Feature data
        KM_y : [array], Target-like data
    Returns:
        KME_labels: [ndarray], shape (n_samples,), cluster assignment for each point
        KME_centers: [ndarray], shape (n_clusters, n_features), cluster centroids
        KME_inertia: [float], sum of squared distances of samples to their closest cluster center
        KME_model: [KMeans object], the trained KMeans model
K_Means_Optimal:
    Parameters:
        KM_x : [array], Feature data
        KM_y : [array], Target-like data
        cluster_nb : [int], Number of clusters to form (default = 3)
        RSEED : [int], Random seed for reproducibility (default = 42)
    Returns:
        KMO_labels: [ndarray], shape (n_samples,), cluster assignment for each point
        KMO_centers: [ndarray], shape (n_clusters, n_features), cluster centroids
        KMO_inertia: [float], sum of squared distances of samples to their closest cluster center
        KMO_model: [KMeans object], the trained KMeans model
"""
def K_Means_Elbow(KM_x, KM_y):
    
    # Turn input values to numpy arrays
    KM_x = np.array(KM_x, dtype=float)
    KM_y = np.array(KM_y, dtype=float)

    # Reshape "y" if data 1D instead of 2D
    if KM_y.ndim == 1:
        KM_y = KM_y.reshape(-1, 1)

    # Combine x and y into a single dataset for clustering
    data = np.column_stack((KM_x, KM_y))

    # Initialize and fit KMeans model
    inertias = []

    # Run KMeans for a range of cluster numbers to visualize the elbow method
    for i in range(1, 11):
        kmeans = KMeans(n_clusters = i, random_state = 42)
        kmeans.fit(data)
        inertias.append(kmeans.inertia_)

    # Plot the elbow method
    plt.plot(range(1, 11), inertias, marker='o')
    plt.title("K-Means elbow method\n(optimal clusters)")
    plt.xlabel("Number of clusters")
    plt.ylabel("Inertia")
    plt.show()

    return kmeans.labels_, kmeans.cluster_centers_, kmeans.inertia_, kmeans

def K_Means_Optimal(KM_x, KM_y, cluster_nb = 3, RSEED = 42):
    
    # Turn input values to numpy arrays
    KM_x = np.array(KM_x, dtype=float)
    KM_y = np.array(KM_y, dtype=float)

    # Reshape "y" if data 1D instead of 2D
    if KM_y.ndim == 1:
        KM_y = KM_y.reshape(-1, 1)

    # Combine x and y into a single dataset for clustering
    data = np.column_stack((KM_x, KM_y))

    # Initialize and fit KMeans model
    kmeans = KMeans(n_clusters = cluster_nb, random_state = RSEED)

    # Fit the model with the data
    kmeans.fit(data)

    return kmeans.labels_, kmeans.cluster_centers_, kmeans.inertia_, kmeans

# -------- FUNCTION CALLBACK EXAMPLE --------

"""
# Define clustering data
KM_x = [1, 2, 3, 4, 5]
KM_y = [2, 4, 5, 4, 5]

# Callback k-means elbow method (for 1–10 clusters)
KME_labels, KME_centers, KME_inertia, KME_model = K_Means_Elbow(KM_x, KM_y)

# Callback and run KMeans function
KMO_labels, KMO_centers, KMO_inertia, KMO_model = K_Means_Optimal(KM_x, KM_y, cluster_nb = 3, RSEED = 42)

# Print results
print("Cluster labels:", KMO_labels)
print("Cluster centers:", KMO_centers)
print("Inertia:", KMO_inertia)
"""
