import seaborn as sns

# Load the dataset
titanic = sns.load_dataset('titanic')

# Calculate the numerical data range
age_range = titanic['age'].max() - titanic['age'].min()
print('Age Range:', age_range)

# Calculate the IQR
Q1 = titanic['age'].quantile(0.25)
Q3 = titanic['age'].quantile(0.75)
IQR = Q3 - Q1
print('Age IQR:', IQR)

# Calculate the median
median_age = titanic['age'].median()
print('Median Age:', median_age)