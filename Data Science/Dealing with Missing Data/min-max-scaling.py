import numpy as np
import seaborn as sns

from sklearn.preprocessing import MinMaxScaler

# Load the dataset and drop rows with missing values
titanic_df = sns.load_dataset('titanic').dropna()

# Initialize the MinMaxScaler
min_max_scaler = MinMaxScaler()

# Fit and transform the 'fare' column
titanic_df['fare'] = min_max_scaler.fit_transform(np.array(titanic_df['fare']).reshape(-1, 1))

# Check the transformed 'fare' column
print(titanic_df['fare'].head())
"""
1     0.139136
3     0.103644
6     0.101229
10    0.032596
11    0.051822
Name: fare, dtype: float64
"""