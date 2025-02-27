# Load the data
import seaborn as sns

titanic_df = sns.load_dataset('titanic')

# Create a new feature, 'family_size'
titanic_df['family_size'] = titanic_df['sibsp'] + titanic_df['parch'] + 1
print(titanic_df.head())
"""
   survived  pclass     sex   age  ...  embark_town  alive  alone family_size
0         0       3    male  22.0  ...  Southampton     no  False           2
1         1       1  female  38.0  ...    Cherbourg    yes  False           2
2         1       3  female  26.0  ...  Southampton    yes   True           1
3         1       1  female  35.0  ...  Southampton    yes  False           2
4         0       3    male  35.0  ...  Southampton     no   True           1

[5 rows x 16 columns]
"""