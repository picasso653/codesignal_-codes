# Import required libraries
import seaborn as sns
import numpy as np

# TODO: Load the Titanic DataSet
titanic_df = sns.load_dataset('titanic')

# TODO: Calculate mean, median, and mode for 'age', print them
print(f"The mean for age: {titanic_df['age'].mean()}")
print(f"The median for age: {titanic_df['age'].median()}")
print(f"The mode for age: {titanic_df['age'].mode()[0]}")
# TODO: Calculate the standard deviation for 'age', print it

print(f"The standard deviation for age: {np.std(titanic_df['age'])}")

# TODO: Calculate Quartiles for 'age', print them
print(f"The first quartile: {titanic_df['age'].quantile(0.25)}")
print(f"The last quartile: {titanic_df['age'].quantile(0.75)}")