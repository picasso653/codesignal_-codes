# Import necessary libraries
import pandas as pd
import seaborn as sns

# Load the dataset
titanic_df = sns.load_dataset('titanic')

# Apply Label Encoding to the 'class' column
titanic_df['class_encoded'] = pd.factorize(titanic_df['class'])[0]
print(titanic_df[['class', 'class_encoded']].head())

# TODO: Apply One-Hot Encoding to the 'who' column
encoded_df = pd.get_dummies(titanic_df['who'], prefix='is')
titanic_df = pd.concat([titanic_df, encoded_df], axis=1)
print(titanic_df[['is_man', "is_woman", 'is_child']].head())