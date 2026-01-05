
# An array is a fundamental data structure in computing that stores a collection of items (like numbers or text) of the same data type in a single, ordered list, using contiguous memory locations, making it easy to access elements by a numerical index (starting from 0).

import numpy as np

# Create arrays

array_1 = np.array([1,2,3,4,5])
print("Array 1:", array_1)
print(type(array_1))

# Check version
print("Numpy Version:", np.__version__)

# Use tuple to create array

array_2 = np.array((6,7,8,9, 10))
print("Array 2:", array_2)