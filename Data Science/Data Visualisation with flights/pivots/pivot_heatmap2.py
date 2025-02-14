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
            cmap='icefire',
            annot=True,
            fmt="d",
            linewidths=1,
            cbar=True,
            center = flights_pivot.loc["Jan", 1955] # Center colormap at the value of passengers in January 1955
)

heatmap.set_title("Heatmap of Monthly Air Travel Data")
plt.show()