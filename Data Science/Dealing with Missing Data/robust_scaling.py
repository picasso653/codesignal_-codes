import numpy as np
import seaborn as sns
from sklearn.preprocessing import RobustScaler

# Initialize the RobustScaler
robust_scaler = RobustScaler()

titanic_df = sns.load_dataset('titanic').dropna()


# Fit and transform the 'fare' column
titanic_df['fare'] = robust_scaler.fit_transform(np.array(titanic_df['fare']).reshape(-1, 1))

# Check the transformed 'fare' column
print(titanic_df['fare'].head())
"""
1     0.236871
3    -0.064677
6    -0.085199
10   -0.668325
11   -0.504975
Name: fare, dtype: float64
"""