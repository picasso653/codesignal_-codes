# Importing necessary libraries
import pandas as pd
import seaborn as sns
from sklearn import preprocessing

# Loading Titanic dataset
titanic_df = sns.load_dataset('titanic')

#label Encoding
titanic_df['alive_encoded'] = pd.factorize(titanic_df['alive'])[0]

# Print the 'alive' and 'alive_encoded' columns
print(titanic_df[['alive', 'alive_encoded']].head())