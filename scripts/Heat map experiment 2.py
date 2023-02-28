import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# import data 
data = pd.read_csv("C:/Users/holst/OneDrive/Dokumenter/GitHub/snake_games/data/test.csv")
df = data

# calculate correlation matrix
corr_matrix = df.corr()

# create heatmap
sns.heatmap(corr_matrix, cmap="binary", annot= True, annot_kws={"fontsize": 10})

# show plot
plt.show()

