import seaborn as sns
import pandas as pd

flights_data = sns.load_dataset("flights")
flights_data['year'] = pd.to_datetime(flights_data['year'], format='%Y')
flights_pivot = pd.pivot_table(data=flights_data, values='passengers', index='year', aggfunc='sum').reset_index()

import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# Extracting the year from the date and converting it into the appropriate format
flights_pivot['year'] = flights_pivot['year'].dt.year

X = np.array(flights_pivot['year']).reshape(-1,1)
y = flights_pivot['passengers']

reg = LinearRegression().fit(X, y)

plt.scatter(X, y, color = "m", marker = "o", s = 30)

Y_pred = reg.predict(X)
plt.plot(X, Y_pred, color = "g")

plt.xlabel('Year')
plt.ylabel('Passengers')
plt.title('Linear Regression: Passengers Over Time')
plt.show()

# Forecast for the next 10 years
new_years = np.array(range(1961, 1971)).reshape(-1,1)
new_passenger_numbers = reg.predict(new_years)
print("Year, Predicted Passengers")
for year, passengers in zip(new_years, new_passenger_numbers):
    print(f"{year[0]}, {int(passengers)}")