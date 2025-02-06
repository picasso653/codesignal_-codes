# Importing required libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Load Titanic dataset
titanic_df = sns.load_dataset('titanic')

# Correlation matrix
correlation_matrix = titanic_df.corr(numeric_only=True)

# Print the correlation matrix
print(correlation_matrix)

# Custom color map
color_map = sns.diverging_palette(220, 20, as_cmap=True)

# Define the size of our plot
plt.figure(figsize=(8, 6))

sns.heatmap(correlation_matrix, annot=True, cmap=color_map)

# Show the plot
plt.show()