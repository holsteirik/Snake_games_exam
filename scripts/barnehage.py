import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind
from scipy.stats import ttest_1samp

# Load the data
data = pd.read_csv("../data/data_barnehage2.csv", delimiter=";")
df = data

# Convert age column to floats
data['alder'] = data['alder'].str.replace(',', '.').astype(float)

# Filter out the rows where age is less than 4
filtered_data = data[data['alder'] >= 4]

# Split the data into two separate data frames
informert = filtered_data[filtered_data['betingelse'] == 'informert']['sum_dyr']
uinformert = filtered_data[filtered_data['betingelse'] == 'uinformert']['sum_dyr']

# Calculate means and standard errors of the means
informert_mean = informert.mean()
uinformert_mean = uinformert.mean()
informert_sem = informert.sem()
uinformert_sem = uinformert.sem()

# Perform an independent t-test assuming unequal variances
t_stat, p_value = ttest_ind(informert, uinformert, equal_var=False)

# Set up the plot
fig, ax = plt.subplots()

# Plot the bar chart
ax.bar(['Informert', 'Uinformert'], [informert_mean, uinformert_mean], yerr=[informert_sem, uinformert_sem], capsize=10)

# Set the y-axis label
ax.set_ylabel('Percentage of type choices')
ax.set_xlabel('Error bars are standard error of the mean')
plt.title('Preference for type')

# Add significance stars
if p_value < 0.05:
    x1, x2 = 0, 1
    y, h, col = 1.1 * max(informert_mean, uinformert_mean), 0.03, 'k'
    ax.plot([x1, x1, x2, x2], [y, y+h, y+h, y], lw=1.5, c=col)
    ax.text((x1+x2)*0.5, y+h, "*", ha='center', va='bottom', color=col, fontsize=20)

# Set the y-tick labels in increments of 10%
ax.set_yticklabels(['0%', '10%', '20%', '30%', '40%', '50%', '60%', '70%', '80%', '90%', '100%'])

# Show the plot
plt.show()

# Print the results
print("t-statistic: ", t_stat)
print("p-value: ", p_value)

# Calculate the mean of informert
informert_mean = informert.mean()

# Perform a one-sample t-test assuming a mean of 6
t_stat, p_value = ttest_1samp(informert, popmean=6)

# Print the results
print("informert mean: ", informert_mean)
print("p-value: ", p_value)
