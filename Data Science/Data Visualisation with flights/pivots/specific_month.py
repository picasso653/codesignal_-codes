# Import necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Load the flights dataset
flights_df = sns.load_dataset('flights')

# Pivot the DataFrame
flights_df_pivot = flights_df.pivot(index="month", columns="year", values="passengers")

# Get the total passenger count for each year
july_totals = flights_df_pivot.loc['Jul']

# Create a line plot of the total passenger count for each year
july_totals.plot(grid=True, figsize=(10,5), linestyle='--')

# Assign the title and labels
plt.title("July Total Passenger Counts (1949 - 1960)")
plt.ylabel("Total Passenger Count")
plt.xlabel("Year")

# Display the plot
plt.show()