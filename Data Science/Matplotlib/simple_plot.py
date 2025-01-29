# Import the necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Titanic dataset
titanic = sns.load_dataset('titanic')

# Count total males and females
gender_data = titanic['sex'].value_counts()

# Plot the 'gender_data'
gender_data.plot(kind='bar', color='skyblue', alpha=0.7, grid=True)

# Title the plot and the axes
plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Frequency")

# Display the plot
plt.show()