# Import seaborn and matplotlib.pyplot libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Load Titanic data from Seaborn library
titanic_df = sns.load_dataset('titanic')

# Create box plot, 'fare' against 'pclass'
sns.boxplot(x='pclass', y='fare', data=titanic_df)

# Set the title for the plot
plt.title('Fares vs Passenger Classes')

# Show the plot
plt.show()