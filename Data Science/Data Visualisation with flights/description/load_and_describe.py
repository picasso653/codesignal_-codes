# Import the necessary library
import seaborn as sns

# Load the Flights dataset
flights_df = sns.load_dataset('flights')

# Display dataset structure
print("First five records of the dataset:")
print(flights_df.head())

# Obtain and display basic statistics of the dataset
print("\nBasic statistics of the dataset:")
print(flights_df.describe())