from sklearn.datasets import fetch_california_housing
import pandas as pd



dataset = fetch_california_housing()


df = pd.DataFrame(data=dataset.data, columns=dataset.feature_names)
df["MedHouseValue"] = dataset.target
print(df.head())
"""
   MedInc  HouseAge  AveRooms  ...  Latitude  Longitude  MedHouseValue
0  8.3252      41.0  6.984127  ...     37.88    -122.23          4.526
1  8.3014      21.0  6.238137  ...     37.86    -122.22          3.585
2  7.2574      52.0  8.288136  ...     37.85    -122.24          3.521
3  5.6431      52.0  5.817352  ...     37.85    -122.25          3.413
4  3.8462      52.0  6.281853  ...     37.85    -122.25          3.422

[5 rows x 9 columns]
"""
print(df.shape) # Output: (20640, 9)
print(df.describe())
"""
             MedInc      HouseAge  ...     Longitude  MedHouseValue
count  20640.000000  20640.000000  ...  20640.000000   20640.000000
mean       3.870671     28.639486  ...   -119.569704       2.068558
std        1.899822     12.585558  ...      2.003532       1.153956
min        0.499900      1.000000  ...   -124.350000       0.149990
25%        2.563400     18.000000  ...   -121.800000       1.196000
50%        3.534800     29.000000  ...   -118.490000       1.797000
75%        4.743250     37.000000  ...   -118.010000       2.647250
max       15.000100     52.000000  ...   -114.310000       5.000010

[8 rows x 9 columns]
"""
print(df.isnull().sum())
"""
MedInc           0
HouseAge         0
AveRooms         0
AveBedrms        0
Population       0
AveOccup         0
Latitude         0
Longitude        0
MedHouseValue    0
dtype: int64
"""