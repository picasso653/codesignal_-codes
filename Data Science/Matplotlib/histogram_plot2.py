# Import the necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Titanic dataset
titanic_df = sns.load_dataset('titanic')

# Create a histogram for the 'age' column with KDE enabled
sns.histplot(data=titanic_df, x='age', kde=True, binwidth=0.5)

# Assign title and axes labels
plt.title('Age Distribution Among Titanic Passengers')
plt.xlabel('Age')
plt.ylabel('Number of Passengers')

# Display the histogram
plt.show()