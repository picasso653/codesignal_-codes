# Import the necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load the flights dataset
flights_data = sns.load_dataset('flights')

# Aggregate passengers' count for each month
month_wise_data = flights_data.groupby('month')['passengers'].sum().reset_index()

# Create a line plot with customized parameters
plt.figure(figsize=(14, 8))
plt.plot(month_wise_data['month'], month_wise_data['passengers'], color='green', alpha=0.7, marker='o', linewidth=2)
plt.title('Month-wise Total Passengers (1949 - 1960)', fontsize=16)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Number of Passengers', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()