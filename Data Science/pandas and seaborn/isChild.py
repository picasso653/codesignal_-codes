# Import the necessary libraries
import pandas as pd
import seaborn as sns

# Load the Titanic dataset
titanic = sns.load_dataset('titanic')

# Print the first 5 rows of the dataset
print(titanic.head())

# TODO: Add a new column that identifies the passengers who are less than 18
titanic['IsChild'] = titanic['age'].apply(lambda x: 'Yes' if x < 18 else 'No')

# TODO: Print the dataset after adding the new column
print("dataset after adding new column: \n",titanic.head())