import numpy as np
import pandas as pd
import seaborn as sns

# Load the dataset
titanic_df = sns.load_dataset('titanic')

# Calculate Z-scores
titanic_df['age_zscore'] = np.abs((titanic_df.age - titanic_df.age.mean()) / titanic_df.age.std())

# Get rows of outliers according to the Z-score method (using a threshold of 3)
outliers_zscore = titanic_df[(titanic_df['age_zscore'] > 3)]
print(outliers_zscore)
"""
     survived  pclass   sex   age  ...  embark_town  alive  alone age_zscore
630         1       1  male  80.0  ...  Southampton    yes   True   3.462699
851         0       3  male  74.0  ...  Southampton     no   True   3.049660

[2 rows x 16 columns]
"""
# Using the Z-score method

titanic_df = titanic_df[titanic_df['age_zscore'] <= 3]