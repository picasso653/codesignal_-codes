# Import required libraries
import seaborn as sns
import pandas as pd

# TODO: Load the Titanic dataset
titanic_db = sns.load_dataset('titanic')

# TODO: Filter data for third-class passengers who survived and are older than 40
filtered = titanic_db[(titanic_db['age'] > 40) & (titanic_db['survived'] == 1) & (titanic_db['pclass'] == 3)]

# TODO: Sort the filtered data by age in ascending order
sorted = filtered.sort_values('age')

# TODO: Print the sorted data
print(sorted.head())