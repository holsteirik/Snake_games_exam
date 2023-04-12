
# Python_kurs

Eirik Holst

## This project is the final exam of course psy-3035. 
All scripts are written in python.



## License

[MIT](https://choosealicense.com/licenses/mit/)

 
## Usage

	run /scripts/kinds_versus_individuals in jupyter notbooks or scripts/data_barnehage in spyder.

Both scripts do the same thing, and is based on the dataset in /data/data_barnehage

## Example
```python
#Import packages
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind
from scipy.stats import ttest_1samp

# Load the data
data = pd.read_csv("../data/data_barnehage.csv", delimiter=";")
df = data

# Convert age column to floats
data['alder'] = data['alder'].str.replace(',', '.').astype(float)

t_stat1, p_value1 = ttest_ind(informert, uinformert, equal_var=False)

print("Independent t-test results:")
print("t-statistic: ", t_stat1)
print("p-value: ", p_value1)
```

## Acknowledgements

 Thank you Jamie.
    Thanks for all the doors you have opened for me

Thank you Steffen and Marie 
    For feedback on my script

## Authorship, how to contribute, and how to cite project provided
Author: Eirik Holst

How to contribute: To contribute to the project, you can fork the repository, make changes to your own copy, and then create a pull request to suggest changes to the original project

How to cite (APA)

Holsteirik, R. (2021). Snake_games_exam. GitHub. https://github.com/holsteirik/Snake_games_exam

## References:
Cimpian, A. & Park, J. J. (2014). Tell Me About Pangolins! Evidence That Children Are Motivated to Learn About Kinds. J Exp Psychol Gen, 143(1), 46-55. https://doi.org/10.1037/a0031687

Holst, E. & Diflefsen, K. (2022). Er barn motivert til å lære om typer eller individer? En replikasjon [Unpublished manuscript]. Institutt for psykologi, Norges Arktiske universitet.

## Screenshot

[![Barplot.png](https://i.postimg.cc/XYS0k72Y/Barplot.png)](https://i.postimg.cc/XYS0k72Y/Barplot.png)

