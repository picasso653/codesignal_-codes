# Import necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load the Titanic dataset
titanic = sns.load_dataset('titanic')

# Implement the Scatter Plot depicting the relationship between 'age' and 'fare' using different marker styles for 'sex' and sizes based on 'fare'
sns.scatterplot(x='age', y='fare', hue='sex', style='pclass', size='fare', sizes=(20, 200), data=titanic)

# Title of the Scatter Plot
plt.title("Age vs Fare (Separate colors for Passenger Class, Different markers for Passenger class and Sizes for Fare)")

# Show the Scatter Plot
plt.show()

# Find correlation between all numeric variables in Titanic dataset
corr_vals = titanic.corr(numeric_only=True)

# Display the Correlation Matrix
print(corr_vals)