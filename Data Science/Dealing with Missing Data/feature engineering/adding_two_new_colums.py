# Import the necessary libraries
import seaborn as sns
import pandas as pd

# Load the Titanic dataset
titanic = sns.load_dataset('titanic')

# Create a new feature, 'family_size', which is a sum of siblings, parents, plus the person themselves (1)
titanic['family_size'] = titanic['sibsp'] + titanic['parch'] + 1

# Create a new feature, 'age_group', which groups ages into different bins
bins = [0, 12, 18, 35, 50, 80]  # Define age ranges
labels = ['Child', 'Teenager', 'Young Adult', 'Adult', 'Senior']  # Labels for the bins
titanic['age_group'] = pd.cut(titanic['age'], bins=bins, labels=labels, right=False)

# Print the first few rows of our dataset to check the engineered features
print(titanic[['sibsp', 'parch', 'family_size', 'age', 'age_group']].head())
