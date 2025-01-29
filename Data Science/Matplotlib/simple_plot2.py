# Import necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
titanic_df = sns.load_dataset('titanic')

# Retrieve the count of each gender
gender_data = titanic_df['pclass'].value_counts()

# Create a bar chart for Sex Distribution
gender_data.plot(kind='bar', color='purple', alpha=0.6, grid=True)
plt.xlabel("Class")
plt.ylabel("Count")
plt.title("Passenger Class Distribution")
plt.show()