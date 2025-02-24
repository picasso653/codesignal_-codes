import numpy as np
import pandas as pd
import seaborn as sns


titanic_df = sns.load_dataset('titanic')

# Calculate IQR
Q1 = titanic_df['age'].quantile(0.25)
Q3 = titanic_df['age'].quantile(0.75)
IQR = Q3 - Q1

# Define Bounds
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Get rows of outliers according to IQR method
outliers_iqr = titanic_df[(titanic_df['age'] < lower_bound) | (titanic_df['age'] > upper_bound)]
print(outliers_iqr)
"""
     survived  pclass   sex   age  ...  embark_town  alive  alone age_zscore
33          0       2  male  66.0  ...  Southampton     no   True   2.498943
54          0       1  male  65.0  ...    Cherbourg     no  False   2.430103
96          0       1  male  71.0  ...    Cherbourg     no   True   2.843141
116         0       3  male  70.5  ...   Queenstown     no   True   2.808721
280         0       3  male  65.0  ...   Queenstown     no   True   2.430103
456         0       1  male  65.0  ...  Southampton     no   True   2.430103
493         0       1  male  71.0  ...    Cherbourg     no   True   2.843141
630         1       1  male  80.0  ...  Southampton    yes   True   3.462699
672         0       2  male  70.0  ...  Southampton     no   True   2.774301
745         0       1  male  70.0  ...  Southampton     no  False   2.774301
851         0       3  male  74.0  ...  Southampton     no   True   3.049660

[11 rows x 16 columns]
"""

# Using the IQR method

# using median

titanic_df.loc[(titanic_df['age'] < lower_bound) | (titanic_df['age'] > upper_bound), 'age'] = titanic_df['age'].median()