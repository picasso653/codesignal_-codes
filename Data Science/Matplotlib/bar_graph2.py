import seaborn as sns
import matplotlib.pyplot as plt

# Load the Titanic dataset
titanic_df = sns.load_dataset('titanic')

# Set a consistent color palette for the plot
sns.set_palette("Blues")

# Create a Countplot with customized parameters
sns.countplot(x='pclass', hue='survived', data=titanic_df, palette='light:cyan', orient='v')

# Add a title to the plot
plt.title('Survival Rates by Passenger Class')

# Display the plot
plt.show()