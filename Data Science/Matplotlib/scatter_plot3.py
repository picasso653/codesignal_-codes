# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Titanic dataset
titanic = sns.load_dataset('titanic')

# TODO: Construct a scatter plot illustrating Age vs Fare.
sns.scatterplot(data=titanic, x='age', y='fare', style='pclass', hue='sex')
plt.title("Age vs Fare")

# Display the plot
plt.show()

# Correlation matrix of variables
# TODO: Calculate the correlation matrix
corr_rel = titanic.corr(numeric_only=True)
print(corr_rel)