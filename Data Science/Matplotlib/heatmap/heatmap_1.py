# Import necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Titanic dataset
titanic_df = sns.load_dataset('titanic')

# Print the first 5 rows of the dataset
print(titanic_df.head())

# Calculate the correlation matrix
correlation_matrix = titanic_df.corr(numeric_only=True)

# Print the correlation matrix
print(correlation_matrix)

# Create a heatmap with the correlation matrix
sns.heatmap(correlation_matrix, annot=True, cbar=True, vmin=-1, vmax=1, cmap='coolwarm')

# Display the plot
plt.show()