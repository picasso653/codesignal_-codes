import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
flights = sns.load_dataset('flights')

# Pivot the dataset
flights_pivot = flights.pivot(index="month", columns="year", values="passengers")
print(flights_pivot)
# Plot a heatmap
# Detailed heat map
heatmap = sns.heatmap(flights_pivot,
            cmap='YlGnBu', # choosing a yellow-green-blue colormap
            annot=True, # Turning on annotations
            fmt="d", # displaying annotations as integer
            linewidths=.5, # Add gridlines with width 0.5
            cbar=True, # Include color bar
            center = flights_pivot.loc["Jan", 1955] # Center colormap at the value of passengers in January 1955
)

heatmap.set_title("Heatmap of Monthly Air Travel Data")
plt.show()