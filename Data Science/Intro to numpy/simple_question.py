# Import required libraries
import numpy as np

array_2d = [[5, 10, 15, 20], [25, 30, 35, 40], [45, 50, 55, 60]]

# TODO: Create a 2D numpy array
two_d = np.array(array_2d)

# TODO: Print the details of the array (dimensions, shape, size, and datatype)
print(f"Dimension: {two_d.ndim}")
print(f"shape: {two_d.shape}")
print(f"Size: {two_d.size}")
print(f"datatype: {two_d.dtype}")

# TODO: Perform indexing and slicing operations to access specific elements and slices of the array
sliced_arr = two_d[1, :]
print(f"sliced: {sliced_arr}")
# TODO: Reshape the array to a different size with the same number of elements. Don't forget to print the reshaped array!
print(two_d.reshape(4,3))