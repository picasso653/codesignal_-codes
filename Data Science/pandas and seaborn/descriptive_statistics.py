# Import the necessary libraries
import seaborn as sns

# Load the dataset
titanic = sns.load_dataset('titanic')

#Show the first few lines of the data
print("First few rows of the Titanic dataset:")
print(titanic.head())

# TODO: Generate descriptive statistics for all continuous variables.
print("Descriptive statistics for all continuous variables")
print(titanic.describe())

# TODO: Generate descriptive statistics for all variables.
print("\nDescriptive statistics for all variables")
print(titanic.describe(include='all'))