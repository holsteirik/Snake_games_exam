import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
import patsy
import numpy as np

# Load the data
data = pd.read_csv("../data/attraction.csv")
df = data


print(df.isnull().sum())
print(df.isin([np.nan, np.inf, -np.inf]).sum())
df.fillna(df.mean, inplace=True)
df.dropna(inplace=True)

# Reshape data to long format
df = pd.melt(data.reset_index(), id_vars=['index'], value_vars=['Attractive_upright', 'Unattractive_upright', 'Attractive_inverted', 'Unattractive_inverted'])

# Rename columns
df.columns = ['subject', 'condition', 'value']

# Create two factors
df[['hotness', 'orientation']] = df['condition'].str.split('_', expand=True)

# Reorder columns
df = df[['subject', 'condition', 'hotness', 'orientation', 'value']]

# Use patsy to create design matrix
design_matrix = patsy.dmatrix('C(hotness)*C(orientation) + C(subject)', df)

# Fit repeated measures ANOVA model
rm_anova = sm.stats.anova_lm(ols('value ~ C(hotness)*C(orientation) + C(subject)', df).fit(), typ=2, anova_test='F')

# Print results
print(rm_anova)
