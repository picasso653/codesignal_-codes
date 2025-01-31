# Import the necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Titanic dataset
titanic = sns.load_dataset('titanic')

# Create a histogram for the 'age' column with Kernel Density Estimation
sns.histplot(data = titanic, x = 'age', kde = True)

# Customize the histogram with a title and labels
plt.title('Histogram Showcasing Age Distribution Among Titanic Passengers')
plt.xlabel('Age')
plt.ylabel('Count')

# Display the plot
plt.show()