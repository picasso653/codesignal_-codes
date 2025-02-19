# Import required libraries
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

titanic_df = sns.load_dataset('titanic')

print("Before bfill Imputation")
print(titanic_df.isnull().sum())

titanic_df['age'].fillna(method='bfill', inplace=True)

print("\n After bfill Imputation")
print(titanic_df.isnull().sum())

plt.figure(figsize=(10,6))
sns.heatmap(titanic_df.isnull(), cmap='plasma')
plt.show()