# Import the necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Titanic dataset
titanic = sns.load_dataset("titanic")

# Set palette to Blues
sns.set_palette("Blues")

# Create a color-coded bar plot for 'sex' with 'survived' hue, specific color and order
sns.countplot(x='sex', hue='survived', data=titanic, palette='light:cyan', order=['female', 'male'])

# Set a title
plt.title('Sex and Survival Rates on Titanic')

# Display the plot
plt.show()