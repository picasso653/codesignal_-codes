# Import necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Load Titanic dataset
titanic = sns.load_dataset('titanic')

# Create a scatter plot with Age on the x-axis, Fare on the y-axis, and pclass used for color
sns.scatterplot(x='age', y='fare', style='sex', size='fare', sizes=(20, 200), hue='pclass', data=titanic)

# Assign the title
plt.title("Age vs Fare (Separate markers for Sex and Sizes for Fare)")

# Display the plot
plt.show()