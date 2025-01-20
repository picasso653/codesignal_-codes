# Import the necessary libraries
import numpy as np

# Create a 1D Numpy array
np_array = np.array([9, 2, 8, 1, 7])

# Access the element at index 2
print("Element at index 2:", np_array[2])

# Slice the array from index 1 to 3
slice_array = np_array[1:4]
print("Slice of the array from index 1 to 3:", slice_array)

# Perform multiplication operation on the array by 5
multiplied_array = np_array * 5
print("Multiplied array result:", multiplied_array)