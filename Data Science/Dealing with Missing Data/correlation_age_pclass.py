# Import the necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

titanic_df = sns.load_dataset('titanic')

# Calculate correlation matrix
correlation_matrix = titanic_df.corr(numeric_only=True)

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm')

# Add title and labels
plt.title('Heatmap of Correlation Matrix for Titanic dataset')
plt.xlabel('Features')
plt.ylabel('Features')

# Display the plot
plt.show()

correlation = correlation_matrix['age']['pclass']
print('Correlation between age and pclass: ', correlation)

if abs(correlation) > 0.5:
    titanic_df = titanic_df.drop('age', axis=1)

# Print the first 5 rows of the cleaned dataframe
print(titanic_df.head())