# Import the necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Load Titanic dataset
titanic_df = sns.load_dataset('titanic')

# Set palette to Blues
sns.set_palette('Blues')

# TODO: Create a plot comparing the 'pclass' variable with the 'survived'. Set 'light:cyan' as pallete and order by descending pclass. Give your plot an appropriate title.
sns.countplot(data=titanic_df, x='pclass', hue='survived', palette='light:cyan', order=[3, 2, 1]).set_title(
    "Survival Rate Amongst Passenger Class")

# TODO: Display the plot
plt.show()