# Import necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
titanic_df = sns.load_dataset('titanic')

# Creating histogram using age column from a data set and coloring based on the sex of passengers
sns.histplot(data=titanic_df, x="age", hue="sex", multiple="stack", palette="pastel", kde=True)

# Add a title and labels to the plot
plt.title('Age Distribution Among Titanic Passengers by Gender')
plt.xlabel('Age')
plt.ylabel('Number of Passengers')

# Display the plot
plt.show()