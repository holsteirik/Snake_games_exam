# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 14:13:17 2023

@author: holst
"""
import numpy as np
import pandas as pd
    
data = pd.read_csv("C:/Users/holst/OneDrive/Dokumenter/GitHub/snake_games/data/grades.csv")
df = data

df.columns

#df.rename(columns = {"Marital status": "martial_status"}, inplace=True)
#df.rename(columns = {"Curricular units 1st sem (credited)": "grades_1st_sem"}, inplace=True)
print(np.corrcoef(Mother's occupation, Age at enrollment))


""
df.shape
df.head
df.columns

"""