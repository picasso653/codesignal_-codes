import matplotlib.pyplot as plt
import seaborn as sns

# Load the flights dataset
flights_data = sns.load_dataset('flights')

# Aggregate passengers' count for each month
month_wise_data = flights_data.groupby('month')['passengers'].sum().reset_index()

# Create line plots
plt.figure(figsize=(14, 8))
plt.plot(month_wise_data['month'], month_wise_data['passengers'], marker='o')
plt.grid(True)
plt.title('Month-wise Number of Passengers (1949 - 1960)', fontsize=14)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Number of Passengers', fontsize=12)
plt.show()