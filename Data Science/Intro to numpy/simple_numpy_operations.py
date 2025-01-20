import numpy as np

# Create a 1D Numpy array
np_array1 = np.array([1, 2, 3])

# Create another 1D Numpy array
np_array2 = np.array([4, 5, 6])

# Print their attributes
print("Array 1 - Shape: ", np_array1.shape, " Size: ", np_array1.size, " Data Type: ", np_array1.dtype)
print("Array 2 - Shape: ", np_array2.shape, " Size: ", np_array2.size, " Data Type: ", np_array2.dtype)

# Perform arithmetic operations
print("Addition: ", np_array1 + np_array2)
print("Subtraction: ", np_array1 - np_array2)
print("Multiplication: ", np_array1 * np_array2)
print("Division: ", np_array1 / np_array2)

# Reshape np_array1 and print the reshaped array
np_array1_reshaped = np_array1.reshape(3, 1)
print("Reshaped Array 1:\n", np_array1_reshaped)