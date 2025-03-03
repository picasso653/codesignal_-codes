# Import required libraries
import seaborn as sns
import pandas as pd
import numpy as np

# Load Titanic dataset
titanic = sns.load_dataset('titanic')

# Create 'fare_per_age' feature
titanic['fare_per_age'] = titanic['fare'] / titanic['age']

# Replace non-number values (NaN or infinity) with 0
titanic['fare_per_age'] = titanic['fare_per_age'].replace([np.nan, np.inf, -np.inf], 0)

# Print the first 10 rows of the titanic dataframe
print(titanic.head(10))
