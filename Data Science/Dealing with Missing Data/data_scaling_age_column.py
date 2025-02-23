# Import the necessary libraries
import seaborn as sns
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
import numpy as np

titanic_df = sns.load_dataset('titanic').dropna()

# Initialize the scalers
std_scaler = StandardScaler()
min_max_scaler = MinMaxScaler()
robust_scaler = RobustScaler()

# Scale the 'age' column of the dataset using Standard Scaler
titanic_df['age_std'] = std_scaler.fit_transform(np.array(titanic_df['age']).reshape(-1, 1))

# Scale the 'fare' column of the dataset using the Min-Max Scaler
titanic_df['age_minmax'] = min_max_scaler.fit_transform(np.array(titanic_df['age']).reshape(-1, 1))

# Scale the 'fare' column of the dataset using Robust Scaler
titanic_df['age_robust'] = robust_scaler.fit_transform(np.array(titanic_df['age']).reshape(-1, 1))

# Print the first 5 rows of the modified dataset
print(titanic_df.head())