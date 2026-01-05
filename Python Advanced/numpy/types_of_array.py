# 0D arrays

import numpy as np

array_0d = np.array(42)
print("0D Array:", array_0d)
print(array_0d.ndim)


# 1D arrays - These are the most common and basic arrays.
array_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:", array_1d)
print(array_1d.ndim)
print("First item: ", array_1d[0])  # Accessing first element
print("Sum of second and fourth items: ", array_1d[1] + array_1d[3])

# 2D arrays
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", array_2d)
print(array_2d.ndim)
print("Element at (1,3): ", array_2d[1, 2])  # Accessing element at row 1, column 2