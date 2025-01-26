# Import seaborn
import seaborn as sns

# Load the Titanic dataset
titanic_df = sns.load_dataset('titanic')

# Print the first five entries of the DataFrame
print('First five entries of the DataFrame:')
print(titanic_df.head())

# Print the count of male and female passengers
print('\nSex distribution:')
print(titanic_df['sex'].value_counts())

# Print the unique and count of unique 'embarked' entries
print('\nUnique entries and count of unique entries in the "embarked" column:')
print('Count:', titanic_df['embarked'].nunique())
print('Entries:', titanic_df['embarked'].unique())