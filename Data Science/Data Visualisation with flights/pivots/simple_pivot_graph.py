# Import necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Load the flights dataset
flights_df = sns.load_dataset('flights')

# Pivot the DataFrame
flights_df_pivot = flights_df.pivot(index="month", columns="year", values="passengers")

# Create a line plot with customizations
flights_df_pivot.plot(grid=True, figsize=(10,5), linestyle='--')

# Assign the title and labels
plt.title("Passenger Counts (1949 - 1960)")
plt.ylabel("Passenger Count")

# Display the plot
plt.show()