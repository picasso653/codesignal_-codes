# TODO: Define a list named chosen_countries with countries selected for the road trip
chosen_countries = ["Japan", "Canada", "Spain", "Germany"]

# TODO: Define a dictionary named country_fuel_costs with fuel costs for countries
country_fuel_costs = {"Japan": 800, "Canada": 200, "Spain": 350, "Germany": 400}
# TODO: Initialize a variable total_fuel_cost to 0
total_fuel_cost = 0

# TODO: Use a for loop to add up the fuel cost for each chosen country
for country in chosen_countries:
    total_fuel_cost += country_fuel_costs[country]
# TODO: Calculate the average fuel cost per country
average = total_fuel_cost/len(chosen_countries)
# TODO: Print the total fuel cost for the road trip
print(f"The total cost for the trip is: ${total_fuel_cost}")
# TODO: Print the average fuel cost per country
print(f"Average cost per country is: ${average}")