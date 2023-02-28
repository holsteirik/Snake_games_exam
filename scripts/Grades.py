# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 14:13:17 2023

@author: holst
"""
import numpy as np
import pandas as pd

# import data 
data = pd.read_csv("C:/Users/holst/OneDrive/Dokumenter/GitHub/snake_games/data/grades.csv")
df = data

# Renaming colums
df.rename(columns = {"Mother's qualification": "mothers_education"}, inplace=True)
df.rename(columns = {"Father's occupation": "fathers_education"}, inplace=True)

# Running corrolation on variables
corr_matrix = np.corrcoef(df["mothers_education"], df["fathers_education"])
print(corr_matrix)



"""
df.shape
df.head
df.columns

"""