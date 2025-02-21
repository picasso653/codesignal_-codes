# Import necessary libraries
import pandas as pd
import seaborn as sns

titanic_df = sns.load_dataset('titanic')


titanic_df['deck_encoded'] = pd.factorize(titanic_df['deck'])[0]
print(titanic_df[['deck', 'deck_encoded']].head())


encoded_df = pd.get_dummies(titanic_df['alone'], prefix='one')
titanic_df = pd.concat([titanic_df, encoded_df], axis=1)
print(titanic_df.head())