# Import necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Load the flights dataset
flights_df = sns.load_dataset('flights')

# Pivot the DataFrame, and calculate the sum of passengers over each year
flights_df_pivot = flights_df.pivot(index="year", columns="month", values="passengers").sum(axis=1)

# Create a line plot with customizations
flights_df_pivot.plot(grid=True, linestyle='--', color='blue')

# Add a title and labels to the plot
plt.title("Yearly Total Passenger Counts (1949 - 1960)")
plt.xlabel("Year")
plt.ylabel("Total Passenger Count")

# Display the plot
plt.show()