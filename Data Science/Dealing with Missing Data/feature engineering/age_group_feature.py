# Import pandas
import pandas as pd
import seaborn as sns

titanic_df = sns.load_dataset('titanic')


# Define the bin edges
age_bins = [0, 12, 18, 30, 45, 100]

# Define the bin labels
age_labels = ['Child', 'Teenager', 'Young Adult', 'Middle Age', 'Senior']

# Create the age group feature
titanic_df['age_group'] = pd.cut(titanic_df['age'], bins=age_bins, labels=age_labels)

# Show the first few rows of the data
print(titanic_df.head())
print(titanic_df['age_group'].value_counts())
"""
   survived  pclass     sex   age  ...  alive  alone  family_size    age_group
0         0       3    male  22.0  ...     no  False            2  Young Adult
1         1       1  female  38.0  ...    yes  False            2   Middle Age
2         1       3  female  26.0  ...    yes   True            1  Young Adult
3         1       1  female  35.0  ...    yes  False            2   Middle Age
4         0       3    male  35.0  ...     no   True            1   Middle Age

[5 rows x 17 columns]
"""