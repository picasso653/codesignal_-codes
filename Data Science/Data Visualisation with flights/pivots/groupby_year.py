import matplotlib.pyplot as plt
import seaborn as sns

# Load the flights dataset
flights_data = sns.load_dataset('flights')

# Year-wise passenger distribution

year_wise_data = flights_data.groupby('year')['passengers'].sum()

year_wise_data.plot(kind='line', marker='o')
plt.xlabel("Year", fontsize=12)
plt.ylabel("Number of Passengers", fontsize=12)
plt.title("Year-wise Number of Passengers (1949 - 1960)", fontsize=14)
plt.grid(True)
plt.show()