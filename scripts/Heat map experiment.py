# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 16:41:46 2023

@author: holst
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the correlation matrix from a CSV file
corr_matrix = pd.read_csv("C:/Users/holst/OneDrive/Dokumenter/GitHub/snake_games/data/test.csv", index_col=0)

# Create a mask to only show the lower triangle of the heatmap
mask = np.zeros_like(corr_matrix)
mask[np.triu_indices_from(mask)] = True

# Set up the figure and plot the heatmap
plt.figure(figsize=(10, 10))
sns.heatmap(corr_matrix, cmap="coolwarm", annot=True, fmt=".2f", mask=mask)

# Add a title and axis labels
plt.title("Correlation Matrix", fontsize=16)
plt.xlabel("Variables", fontsize=14)
plt.ylabel("Variables", fontsize=14)

# Show the plot
plt.show()


