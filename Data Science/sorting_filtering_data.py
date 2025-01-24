# Importing required libraries
import seaborn as sns
import pandas as pd

# Load Titanic dataset
titanic_df = sns.load_dataset('titanic')

# Filter male passengers who survived
male_survivors = titanic_df[
    (titanic_df['survived'] == 1) & (titanic_df['sex'] == 'male')
]

# Sort survivors by class and age
sorted_df = male_survivors.sort_values(['pclass', 'age'], ascending=[False, True])

# Display the first 5 rows of the sorted DataFrame
print(sorted_df.head())