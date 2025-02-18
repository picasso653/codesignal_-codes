# Required Libraries
import seaborn as sns
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Loading the 'flights' dataset
flights_data = sns.load_dataset("flights")

# Pivot the dataset to sum passengers yearly
flights_pivot = pd.pivot_table(flights_data, values='passengers', index='year', aggfunc='sum').reset_index()

# Prepare data for model fitting
X = np.array(flights_pivot['year']).reshape(-1,1)
y = flights_pivot['passengers']

# TODO: Fit the Linear Regression model and predict the passenger count for the decade of 1971 to 1980
reg = LinearRegression().fit(X, y)
new_years = np.array(range(1971, 1981)).reshape(-1, 1)
new_passenger_numbers = reg.predict(new_years)

# Print Year and Predicted Passengers
for year, passengers in zip(new_years, new_passenger_numbers):
    print(f"Year: {year[0]}, Predicted Passengers: {int(passengers)}")

# Plot Original data as a scatter plot and a Regression line
plt.scatter(X, y, color='blue')
# TODO: Add the predictions to the plot as a Regression line
Y_pred = reg.predict(X)
plt.plot(X, Y_pred, color = "g")

# Plot labels and title
plt.xlabel("Year")
plt.ylabel("Total Passengers")
plt.title("Historical and Predicted Airline Passengers Over Time")

# Show the plot
plt.show()