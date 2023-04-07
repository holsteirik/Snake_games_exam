
# Python_exam

Exam psy-3035 
Eirik Holst

This project is the final exam of in the course psy-3035. 
All scripts are written in python.

How to use this project
	1. Download files from https://github.com/holsteirik/Snake_games_exam
	2. Run /scripts/kinds_versus_individuals in jupyter notbooks or scripts/data_barnehage in spyder.

Both scripts do the same thing, and use the dataset /data/data_barnehage.

## License

[MIT](https://choosealicense.com/licenses/mit/)

Code 
## Usage/Examples

```python
#Import packages
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind
from scipy.stats import ttest_1samp

# Load the data
data = pd.read_csv("../data/data_barnehage.csv", delimiter=";")

# Convert age column to floats
data['alder'] = data['alder'].str.replace(',', '.').astype(float)

t_stat1, p_value1 = ttest_ind(informert, uinformert, equal_var=False)

print("Independent t-test results:")
print("t-statistic: ", t_stat1)
print("p-value: ", p_value1)


## Acknowledgements

 Thank you Jamie.
    For opening so many doors for me

Thank you Steffen and Marie 
    For feedback on my script

## Documentation

[Documentation](https://github.com/holsteirik/Snake_games_exam)

All code was written by Eirik Holst 2023

References to data used an experiment it was based on:
Cimpian, A. & Park, J. J. (2014). Tell Me About Pangolins! Evidence That Children Are Motivated to Learn About Kinds. J Exp Psychol Gen, 143(1), 46-55. https://doi.org/10.1037/a0031687

Holst, E. & Diflefsen, K. (2022). Er barn motivert til å lære om typer eller individer? En replikasjon [Unpublished manuscript]. Institutt for psykologi, Norges Arktiske universitet.
## Screenshots

![Barplot Screenshot](https://postimg.cc/0bf38xRT)

