import pandas as pd
import seaborn as sns

# Load the Titanic dataset into a pandas DataFrame
titanic_df = sns.load_dataset('titanic')

# Add a column to dataframe indicating if the passenger is an adult or child
titanic_df["IsAdult"] = titanic_df["age"].apply(lambda x: "No" if x < 18 else "Yes")

# Display the first 5 rows of the DataFrame with the new column
print(titanic_df.head())