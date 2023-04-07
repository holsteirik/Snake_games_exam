import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind
from scipy.stats import ttest_1samp

# Load the data
data = pd.read_csv("../data/data_barnehage.csv", delimiter=";")
df = data

# Convert age column to floats
data['alder'] = data['alder'].str.replace(',', '.').astype(float)

# Filter out the rows where age is less than 4
filtered_data = data[data['alder'] < 4]

# Split the data into two separate data frames
informert = filtered_data[filtered_data['betingelse'] == 'informert']['sum_dyr']
uinformert = filtered_data[filtered_data['betingelse'] == 'uinformert']['sum_dyr']

# Calculate means and standard errors of the means
informert_mean = informert.mean()
uinformert_mean = uinformert.mean()
informert_sem = informert.sem()
uinformert_sem = uinformert.sem()

# Perform an independent t-test assuming unequal variances
t_stat1, p_value1 = ttest_ind(informert, uinformert, equal_var=False)

# Set up the plot
fig, ax = plt.subplots(figsize=(7,8))

ax.bar(["Informed", "Uninformed"], [informert_mean, uinformert_mean], 
       yerr=[informert_sem, uinformert_sem],
       capsize=10, color="#1d5dec")

# Set the y-axis label
ax.set_ylabel("Number of type choices", fontdict={"fontsize": 14, "fontweight": "bold", "fontfamily": "serif"})
ax.set_xlabel("Note: * is significans at .05 level. Error bars are standard error of the mean")
plt.title("Preference for type", fontdict={"fontsize": 14, "fontweight": "bold", "fontfamily": "serif"})

# Add significance stars
if p_value1 < 0.05:
    x1, x2 = 0, 1
    y, h, col = 1.1 * max(informert_mean, uinformert_mean), 0.15, 'k'
    ax.plot([x1, x1, x2, x2], [y, y+h, y+h, y], lw=1.5, c=col)
    ax.text((x1+x2)*0.5, y+h, "*", ha='center', va='bottom', color=col, fontsize=20)

# Set the y-tick labels in increments of 10%
#ax.set_yticklabels(['0%', '10%', '20%', '30%', '40%', '50%', '60%', '70%', '80%', '90%', '100%'])

# Show the plot
plt.show()

# Print the results of the independent t-test
print("Independent t-test results:")
print("t-statistic: ", t_stat1)
print("p-value: ", p_value1)

# Perform a one-sample t-test assuming a mean of 6
t_stat2, p_value2 = ttest_1samp(informert, popmean=6)

# Calculate degrees of freedom
degrees_of_freedom1 = len(informert) + len(uinformert) - 2
degrees_of_freedom2 = len(informert) - 1

# Print the results
print("t-value: ", t_stat2)
print("p-value2: ", p_value2)

if p_value1 < 0.05:
    if p_value2 > 0.05:
        print(f"The manipulation led to a significant difference between conditions "
              f"t({degrees_of_freedom1}) = {t_stat1:.2f}, p = {p_value1:.3f}). However, "
              f"the children in the informed condition did not pick Type significantly "
              f"more often than chance t({degrees_of_freedom2}) = {t_stat2:.2f}, p = {p_value2:.3f}.")
    if p_value2 < 0.05:
        print(f"The manipulation led to a significant difference between conditions "
              f"t({degrees_of_freedom1}) = {t_stat1:.2f}, p = {p_value1:.3f}), and "
              f"children in the informed condition picked Type significantly more often "
              f"than chance t({degrees_of_freedom2}) = {t_stat2:.2f}, p = {p_value2:.3f}.")
else:
    print(f"The manipulation did not lead to any significant differences between the conditions "
          f"t({degrees_of_freedom1}) = {t_stat1:.2f}, p = {p_value1:.3f}).")

